from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import crud, models, schemas
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
        raise Exc.InvalidUsernameOrPasswordException
    if not verify_password(password, user.password):
        raise Exc.InvalidUsernameOrPasswordException
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.JWT_TOKEN_ALGORITHM)
    return encoded_jwt

def decode_access_token(db: Session, token: str) -> schemas.User:
    if token is None or token == '':
        raise Exc.InvalidCredentialsException
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[
                             settings.JWT_TOKEN_ALGORITHM])
        user_id: str = payload.get("id")
        if id is None:
            raise Exc.InvalidCredentialsException
    except JWTError:
        raise Exc.InvalidCredentialsException
    user_db = crud.get_user_by_id(db, user_id)
    if user_db is None:
        raise Exc.InvalidCredentialsException
    return user_db


def admin_required(user: models.User) -> None:
    if not user.is_admin:
        raise Exc.AdminRequiredException
