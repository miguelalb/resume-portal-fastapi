from app import crud
from app.dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/me")
async def get_user_me():
    return "Ok - User Me!"
