from app import crud, schemas
from app.dependencies import get_db
from app.security import authenticate_user, create_access_token
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    token = create_access_token({"id": str(user.id)})
    return schemas.Token(access_token=token, token_type="Bearer")


@router.post("/register")
async def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.create_user(db, user_in)
    return user
