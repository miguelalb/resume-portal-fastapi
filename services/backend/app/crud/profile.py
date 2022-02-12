from typing import List

from app import models, schemas
from app.crud.crud_base import create_generic_profile_child, delete_generic
from app.exceptions import Exc
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def get_user_profile_by_public_name(db: Session, public_name: str):
    return db.query(models.UserProfile)\
        .filter(models.UserProfile.public_name == public_name).first()


def get_user_profile_by_id(db: Session, id: str):
    return db.query(models.UserProfile)\
        .filter(models.UserProfile.id == id).first()


def validate_publicname(db: Session, public_name: str):
    user_profile_inDB = get_user_profile_by_public_name(db, public_name)
    if user_profile_inDB is not None:
        raise Exc.NameTakenException("Public name")


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


def update_each_or_create(
    db: Session, model, incoming_objects: List, profile_id: str):
    for obj_in in incoming_objects:
        if not obj_in.deleted:
            if hasattr(obj_in, "id") and obj_in.id is not None:
                old_object_inDB = db.query(model).filter(
                    model.id == obj_in.id).update(obj_in.dict())
            else:
                create_generic_profile_child(db, model, obj_in, profile_id)


def filter_out_removed(db: Session, model, incoming_objects: List):
    for obj_in in incoming_objects:
        if obj_in.deleted:
            delete_generic(db, model, obj_in.id)  


def update_user_profile(db: Session, profile_in: schemas.UserProfileUpdate, user_id: str):
    profile_inDB = get_user_profile_by_id(db, profile_in.id)
    if profile_inDB is None:
        raise Exc.ObjectNotFoundException("User Profile")
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

    # Update, Create new and Delete removed
    update_each_or_create(db, models.Skill, profile_in.skills, profile_in.id)
    filter_out_removed(db, models.Skill, profile_in.skills)

    update_each_or_create(db, models.Job, profile_in.jobs, profile_in.id)
    filter_out_removed(db, models.Job, profile_in.jobs)
    
    update_each_or_create(db, models.Education, profile_in.educations, profile_in.id)
    filter_out_removed(db, models.Education, profile_in.educations)
    
    update_each_or_create(db, models.Certification, profile_in.certifications, profile_in.id)
    filter_out_removed(db, models.Certification, profile_in.certifications)

    db.commit()
    db.refresh(profile_inDB)
    return profile_inDB


def delete_user_profile(db: Session, profile_id: str):
    delete_generic(db, models.UserProfile, profile_id)
