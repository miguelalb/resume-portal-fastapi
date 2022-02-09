from typing import Optional

from app import crud, schemas
from app.dependencies import get_db
from app.security import decode_access_token
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/me", response_model=schemas.User)
async def get_user_me(token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    print("----- The user Object ----")
    print(user)
    print(user.id)
    print(type(user.id))
    return schemas.User.from_orm(user)

@router.put("/")
async def update_user_me(user_in: schemas.UserUpdate, token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user_inDB = decode_access_token(db, token)
    updated_user = crud.update_user(db, user_in, user_inDB.id)
    return schemas.User.from_orm(updated_user)
