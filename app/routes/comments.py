from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_comments():
    return [
        {"this is a comment mate"},

    ]
