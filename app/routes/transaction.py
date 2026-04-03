from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter()

# CREATE
@router.post("/")
def create_transaction(data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, data)

# GET ALL
@router.get("/")
def get_all_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)