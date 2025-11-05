from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_cases():
    return [
        {"id": 1, "title": "Mysterious Case", "solved": False},
        {"id": 2, "title": "Unsolved Mystery", "solved": True},
        {"id": 3, "title": "The Murder of Mark Barrett by Ashley Fitzgerald", "solved": True}
    ]
