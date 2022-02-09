from typing import Optional

from app import schemas
from app.dependencies import get_db
from app.security import decode_access_token
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/me", response_model=schemas.User)
async def get_user_me(token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    return schemas.User.from_orm(user)
