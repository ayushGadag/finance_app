from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
from app.models import Transaction
from app.utils.roles import check_admin

router = APIRouter()

# ✅ CREATE (Admin only)
@router.post("/")
def create_transaction(
    data: schemas.TransactionCreate,
    role: str,
    db: Session = Depends(get_db)
):
    if not check_admin(role):
        raise HTTPException(status_code=403, detail="Only admin can create")

    return crud.create_transaction(db, data)


# ✅ GET ALL + FILTER
@router.get("/")
def get_transactions(
    type: str = Query(None),
    category: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Transaction)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    return query.all()


# ✅ UPDATE (Admin only)
@router.put("/{transaction_id}")
def update_transaction(
    transaction_id: int,
    data: schemas.TransactionCreate,
    role: str,
    db: Session = Depends(get_db)
):
    if not check_admin(role):
        raise HTTPException(status_code=403, detail="Only admin can update")

    txn = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Not found")

    txn.amount = data.amount
    txn.type = data.type
    txn.category = data.category
    txn.note = data.note

    db.commit()
    db.refresh(txn)

    return txn


# ✅ DELETE (Admin only)
@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    role: str,
    db: Session = Depends(get_db)
):
    if not check_admin(role):
        raise HTTPException(status_code=403, detail="Only admin can delete")

    txn = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not txn:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(txn)
    db.commit()

    return {"message": "Deleted successfully"}