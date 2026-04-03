from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_transaction():
    return {"msg": "transaction working"}