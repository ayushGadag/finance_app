from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_summary():
    return {"msg": "summary working"}