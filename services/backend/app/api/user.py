from app import crud
from app.dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{id}")
def get_user_by_id(id: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    return "Ok - User by ID!"

@router.get("/me")
def get_user_me():
    return "Ok - User Me!"
