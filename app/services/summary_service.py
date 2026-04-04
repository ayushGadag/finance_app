from sqlalchemy.orm import Session
from app.models import Transaction

def calculate_summary(db: Session):
    transactions = db.query(Transaction).all()

    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expense = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }