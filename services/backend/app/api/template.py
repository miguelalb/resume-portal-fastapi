from typing import List, Optional

from app import crud, schemas
from app.dependencies import get_admin_user, get_db, get_user
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=List[schemas.Template])
async def get_all_templates(
    user = Depends(get_user), db: Session = Depends(get_db)):
    templates_obj = crud.get_templates(db, user)
    return [schemas.Template.from_orm(obj) for obj in templates_obj]


@router.post(
    "",
    response_model=schemas.Template, status_code=status.HTTP_201_CREATED)
async def create_template(
    template: schemas.TemplateCreate,
    admin = Depends(get_admin_user), db: Session = Depends(get_db)):
    template_obj = crud.create_template(db, template)
    return schemas.Template.from_orm(template_obj)


@router.put("", response_model=schemas.Template)
async def update_template(
    template_id: str, template: schemas.TemplateCreate,
    admin = Depends(get_admin_user), db: Session = Depends(get_db)):
    template_obj = crud.update_template(db, template, template_id)
    return schemas.Template.from_orm(template_obj)


@router.get("/{template_id}", response_model=schemas.Template)
async def get_template_by_id(
    template_id: str,
    user = Depends(get_user), db: Session = Depends(get_db)):
    template_obj = crud.get_template_by_id_out(db, template_id, user)
    return schemas.Template.from_orm(template_obj)


@router.delete("/{template_id}", response_model=schemas.GenericMessage)
async def update_template(
    template_id: str,
    admin = Depends(get_admin_user), db: Session = Depends(get_db)):
    template_obj = crud.delete_template(db, template_id)
    return schemas.GenericMessage(message="Template deleted successfully!")
