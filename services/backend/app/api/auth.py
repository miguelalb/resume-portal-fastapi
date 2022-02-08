from app import crud, schemas
from app.dependencies import get_db
from app.security import authenticate_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    # TODO Generate JWT Token
    return schemas.User.from_orm(user)


@router.post("/register")
async def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.create_user(db, user_in)
    return user
