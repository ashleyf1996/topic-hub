from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_users():
    return [
        {"this is a user mate"},

    ]