from app import crud, schemas
from app.dependencies import get_db
from app.security import authenticate_user, create_access_token
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/login")
async def login(user_in: schemas.UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.username, user_in.password)
    token = create_access_token({"id": str(user.id)})
    return schemas.Token(access_token=token, token_type="Bearer")


@router.post(
    "/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED
)
async def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.create_user(db, user_in)
    return schemas.User.from_orm(user)
