from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import crud
from app.config import get_settings
from app.exceptions import Exc

settings = get_settings()

pwd_context = CryptContext(schemes=[settings.CRYP_SCHEME], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise Exc.InvalidCredentialsException
    if not verify_password(password, user.password):
        raise Exc.InvalidCredentialsException
    return user
