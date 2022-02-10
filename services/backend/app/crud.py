from typing import List

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
    return user_obj


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

def get_user_profile_by_id(db: Session, id: str):
    return db.query(models.UserProfile)\
        .filter(models.UserProfile.id == id).first()


def validate_publicname(db: Session, public_name: str):
    user_profile_inDB = get_user_profile_by_public_name(db, public_name)
    if user_profile_inDB is not None:
        raise Exc.PublicNameTakenException


def create_user_profile(
    db: Session, profile_in: schemas.UserProfileCreate, user_id: str):
    validate_publicname(db, profile_in.public_name)
    
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

def create_skill(db: Session, skill: schemas.SkillCreate, profile_id: str):
    skill_obj = models.Skill(**skill.dict())
    db.add(skill_obj)
    skill_obj.profile_id = profile_id
    db.commit()


def create_job(db: Session, job: schemas.JobCreate, profile_id: str):
    job_obj = models.Job(**job.dict())
    db.add(job_obj)
    job_obj.profile_id = profile_id
    db.commit()


def create_education(db: Session, education: schemas.EducationCreate, profile_id: str):
    education_obj = models.Education(**education.dict())
    db.add(education_obj)
    education_obj.profile_id = profile_id
    db.commit()


def create_certification(db: Session, certification: schemas.CertificationCreate, profile_id: str):
    certification_obj = models.Certification(**certification.dict())
    db.add(certification_obj)
    certification_obj.profile_id = profile_id
    db.commit()


MODEL_CREATE_MAPPING = {
    "skill": create_skill,
    "job": create_job,
    "education": create_education,
    "certification": create_certification
}

def update_each_or_create(
    db: Session, model, incoming_objects: List, model_type: str, profile_id: str):
    for obj_in in incoming_objects:
        if hasattr(obj_in, "id") and obj_in.id is not None:
            old_object_inDB = db.query(model).filter(
                model.id == obj_in.id).update(obj_in.dict())
        else:
            fn = MODEL_CREATE_MAPPING[model_type]
            fn(db, obj_in, profile_id)


def update_user_profile(db: Session, profile_in: schemas.UserProfileUpdate, user_id: str):
    profile_inDB = get_user_profile_by_id(db, profile_in.id)
    if profile_inDB is None:
        raise Exc.ProfileNotFoundException
    if profile_inDB.public_name != profile_in.public_name:
        validate_publicname(db, profile_in.public_name)
    profile_inDB.first_name = profile_in.first_name
    profile_inDB.last_name = profile_in.last_name
    profile_inDB.public_name = profile_in.public_name
    profile_inDB.theme = profile_in.theme
    profile_inDB.summary = profile_in.summary
    profile_inDB.email = profile_in.email
    profile_inDB.phone = profile_in.phone
    profile_inDB.designation = profile_in.designation

    update_each_or_create(db, models.Skill, profile_in.skills, "skill", profile_in.id)
    update_each_or_create(db, models.Job, profile_in.jobs, "job", profile_in.id)
    update_each_or_create(db, models.Education, profile_in.educations, "education", profile_in.id)
    update_each_or_create(db, models.Certification, profile_in.certifications, "certification", profile_in.id)

    db.commit()
    db.refresh(profile_inDB)
    return profile_inDB
