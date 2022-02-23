from typing import Optional

from app import crud, schemas
from app.dependencies import get_admin_user, get_db, get_user
from app.security import decode_access_token
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/me", response_model=schemas.User)
async def get_user_me(
    user = Depends(get_user), db: Session = Depends(get_db)):
    return schemas.User.from_orm(user)


@router.put("")
async def update_user_me(
    user_in: schemas.UserUpdate,
    user = Depends(get_user), db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_in, user.id)
    return schemas.User.from_orm(updated_user)

