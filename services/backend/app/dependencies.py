from typing import Optional

from fastapi import Depends, Header
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.security import admin_required, decode_access_token


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(
    token: Optional[str] = Header(None),
    db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    return user


def get_admin_user(user = Depends(get_user)):
    admin_required(user)
    return user
