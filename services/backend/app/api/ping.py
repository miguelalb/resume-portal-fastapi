from app.config import get_settings
from fastapi import APIRouter

router = APIRouter()

settings = get_settings()

@router.get("/")
def ping():
    return {
        "ping": "pong!",
        "environment": settings.ENVIRONMENT
    }
