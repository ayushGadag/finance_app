from sqlalchemy.orm import Session
from app.models import Transaction

def create_transaction(db: Session, data):
    new_txn = Transaction(**data.dict())
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return new_txn


def get_transactions(db: Session):
    return db.query(Transaction).all()