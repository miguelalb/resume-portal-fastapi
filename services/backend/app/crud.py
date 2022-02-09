from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models, schemas
from app.exceptions import Exc
from app.security import get_password_hash


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User)\
        .filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User)\
        .filter(models.User.username == username).first()


def create_user(db: Session, user_in: schemas.UserCreate):
    user_inDB = get_user_by_username(db, user_in.username)
    if user_inDB is not None:
        raise Exc.UsernameTakenException
    password_hash = get_password_hash(user_in.password)
    user_obj = models.User(
        username=user_in.username,
        password=password_hash
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return schemas.User.from_orm(user_obj)


def update_user(db: Session, user_in: schemas.UserUpdate, user_id: str):
    user_obj = get_user_by_id(db, user_id)
    if user_obj is None:
        raise Exc.UserNotFoundException
    user_obj.username = user_in.username
    user_obj.password = get_password_hash(user_in.password)
    db.commit()
    db.refresh(user_obj)
    return user_obj


def get_user_profile_by_public_name(db: Session, public_name: str):
    return db.query(models.UserProfile)\
        .filter(models.UserProfile.public_name == public_name).first()


def create_user_profile(
    db: Session, profile_in: schemas.UserProfileCreate, user_id: str):
    user_profile_inDB = get_user_profile_by_public_name(db, profile_in.public_name)
    if user_profile_inDB is not None:
        raise Exc.PublicNameTakenException
    
    user_profile_object = models.UserProfile(
       first_name=profile_in.first_name,
       last_name=profile_in.last_name,
       public_name=profile_in.public_name,
       theme=profile_in.theme,
       summary=profile_in.summary,
       email=profile_in.email,
       phone=profile_in.phone,
       designation=profile_in.designation
    )
    db.add(user_profile_object)
    user_profile_object.user_id = user_id
    
    if profile_in.skills and len(profile_in.skills) > 0:
        for skill in profile_in.skills:
            skill_in = jsonable_encoder(skill)
            db_skill = models.Skill(**skill_in)
            user_profile_object.skills.append(db_skill)

    if profile_in.jobs and len(profile_in.jobs) > 0:
        for job in profile_in.jobs:
            job_in = jsonable_encoder(job)
            db_job = models.Job(**job_in)
            user_profile_object.jobs.append(db_job)
    
    if profile_in.educations and len(profile_in.educations) > 0:
        for education in profile_in.educations:
            education_in = jsonable_encoder(education)
            db_education = models.Education(**education_in)
            user_profile_object.educations.append(db_education)
    
    if profile_in.certifications and len(profile_in.certifications) > 0:
        for certification in profile_in.certifications:
            certification_in = jsonable_encoder(certification)
            db_certification = models.Certification(**certification_in)
            user_profile_object.certifications.append(db_certification)
    
    db.commit()
    db.refresh(user_profile_object)
    return user_profile_object
