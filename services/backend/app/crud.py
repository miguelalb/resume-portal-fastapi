from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models, schemas
from app.exceptions import Exc
from app.security import get_password_hash


def create_generic_profile_child(db: Session, model, object_in, profile_id: str):
    model_obj = model(**object_in.dict())
    db.add(model_obj)
    model_obj.profile_id = profile_id
    db.commit()


def delete_generic(db: Session, model, obj_id: str):
    model_obj = db.query(model).filter(model.id == obj_id).first()
    if model_obj is None:
        raise Exc.ObjectNotFoundException("Object")
    db.delete(model_obj)
    db.commit()


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.User)\
        .filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User)\
        .filter(models.User.username == username).first()


def create_user(db: Session, user_in: schemas.UserCreate):
    user_inDB = get_user_by_username(db, user_in.username)
    if user_inDB is not None:
        raise Exc.NameTakenException("Username")
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


def get_templates(db: Session, user: models.User):
    if user.is_premium:
        return db.query(models.Template).all()
    return db.query(models.Template)\
        .filter(models.Template.premium == False).all()


def get_template_by_id(db: Session, id: str):
    return db.query(models.Template)\
        .filter(models.Template.id == id).first()


def get_template_by_name(db: Session, name: str):
    return db.query(models.Template)\
        .filter(models.Template.name == name).first()


def create_template(db: Session, template_in: schemas.TemplateCreate):
    existing_template = get_template_by_name(db, template_in.name)
    if existing_template is not None:
        raise Exc.NameTakenException("Template name")
    template_obj = models.Template(**template_in.dict())
    db.add(template_obj)
    db.commit()
    db.refresh(template_obj)
    return template_obj


def update_template(db: Session, template_in: schemas.TemplateUpdate, template_id: str):
    template_obj = get_template_by_id(db, template_id)
    if template_obj is None:
        raise Exc.ObjectNotFoundException("Template")
    
    template_obj.name = template_in.name
    template_obj.content = template_in.content
    template_obj.premium = template_in.premium
    db.commit()
    db.refresh(template_obj)
    return template_obj


def delete_template(db: Session, template_id: str):
    delete_generic(db, models.Template, template_id)
