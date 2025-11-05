from fastapi import APIRouter

router = APIRouter()

@router.get("")
def get_channels():
    return [
        {"yo man channels "},
       
    ]
