from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_user():
    return {"msg": "user working"}