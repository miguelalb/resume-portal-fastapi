from sqlalchemy.orm import Session

from app import models
from app.exceptions import Exc


def get_user_by_id(db: Session, user_id: str):
    user = db.query(models.User)\
        .filter(models.user.id == user_id).first()
    if user is None:
        raise Exc.UserNotFoundException

def create_user(db: Session, user):
    pass

def get_user_profile_by_public_name(db: Session, public_name: str):
    user_profile = db.query(models.UserProfile)\
        .filter(models.UserProfile.public_name == public_name).first()
    if user_profile is None:
        raise Exc.ProfileNotFoundException
    return user_profile

