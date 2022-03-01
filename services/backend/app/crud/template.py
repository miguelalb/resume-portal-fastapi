from app import models, schemas
from app.crud.crud_base import delete_generic
from app.exceptions import Exc
from sqlalchemy.orm import Session


def get_templates(db: Session, user: models.User):
    if user.is_premium:
        return db.query(models.Template).all()
    return db.query(models.Template).filter(models.Template.premium == False).all()


def get_all_templates_internal(db: Session):
    return db.query(models.Template).all()


def get_template_by_id(db: Session, id: str):
    return db.query(models.Template).filter(models.Template.id == id).first()


def get_template_by_id_out(db: Session, template_id: str, user: models.User):
    if user.is_premium:
        return (
            db.query(models.Template).filter(models.Template.id == template_id).first()
        )
    return (
        db.query(models.Template)
        .filter(models.Template.premium == False)
        .filter(models.Template.id == template_id)
        .first()
    )


def get_template_by_name(db: Session, name: str):
    return db.query(models.Template).filter(models.Template.name == name).first()


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
