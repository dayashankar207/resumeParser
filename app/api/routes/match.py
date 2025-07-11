from fastapi import APIRouter

router = APIRouter()

# You can now define matching routes here
@router.get("/")
def test_match():
    return {"msg": "match route working"}
