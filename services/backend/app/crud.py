from sqlalchemy.orm import Session

from app import models, schemas
from app.exceptions import Exc
from app.security import get_password_hash


def get_user_by_id(db: Session, user_id: str):
    user = db.query(models.User)\
        .filter(models.User.id == user_id).first()
    if user is None:
        raise Exc.UserNotFoundException

def get_user_by_username(db: Session, username: str):
    return db.query(models.User)\
        .filter(models.User.username == username).first()

def create_user(db: Session, user_in: schemas.UserCreate):
    password_hash = get_password_hash(user_in.password)
    user_obj = models.User(
        username=user_in.username,
        password=password_hash
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return schemas.User.from_orm(user_obj)

def get_user_profile_by_public_name(db: Session, public_name: str):
    user_profile = db.query(models.UserProfile)\
        .filter(models.UserProfile.public_name == public_name).first()
    if user_profile is None:
        raise Exc.ProfileNotFoundException
    return user_profile

