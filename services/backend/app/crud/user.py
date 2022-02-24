from app import models, schemas
from app.crud.crud_base import delete_generic
from app.exceptions import Exc
from app.security import get_password_hash
from sqlalchemy.orm import Session


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user_in: schemas.UserCreate):
    user_inDB = get_user_by_username(db, user_in.username)
    if user_inDB is not None:
        raise Exc.NameTakenException("Username")
    password_hash = get_password_hash(user_in.password)
    user_obj = models.User(username=user_in.username, password=password_hash)
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


def update_user(db: Session, user_in: schemas.UserUpdate, user_id: str):
    user_obj = get_user_by_id(db, user_id)
    if user_obj is None:
        raise Exc.ObjectNotFoundException("User")
    user_obj.username = user_in.username
    user_obj.password = get_password_hash(user_in.password)
    db.commit()
    db.refresh(user_obj)
    return user_obj


def delete_user(db: Session, user_id: str):
    delete_generic(db, models.User, user_id)


def promote_user(db: Session, user_id: str):
    user_obj = get_user_by_id(db, user_id)
    if user_obj is None:
        raise Exc.ObjectNotFoundException("User")
    user_obj.is_admin = True
    db.commit()
    db.refresh(user_obj)
    return user_obj


def upgrade_user_to_premium(db: Session, user_id: str):
    user_obj = get_user_by_id(db, user_id)
    if user_obj is None:
        raise Exc.ObjectNotFoundException("User")
    user_obj.is_premium = True
    db.commit()
    db.refresh(user_obj)
    return user_obj
