from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.summary_service import calculate_summary

router = APIRouter()

@router.get("/")
def get_summary(db: Session = Depends(get_db)):
    return calculate_summary(db)