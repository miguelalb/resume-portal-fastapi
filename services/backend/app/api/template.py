from typing import List, Optional

from app import crud, schemas
from app.dependencies import get_db
from app.security import admin_required, decode_access_token
from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=schemas.Template)
async def get_all_templates(
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    templates_obj = crud.get_templates(db, user)
    return schemas.Template.from_orm(templates_obj)


@router.get("/{template_id}", response_model=schemas.Template)
async def get_template_by_id(
    template_id: str,
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    template_obj = crud.get_template_by_id_out(db, template_id, user)
    return schemas.Template.from_orm(template_obj)


@router.post(
    "/", response_model=schemas.Template, status_code=status.HTTP_201_CREATED)
async def create_template(
    template: schemas.TemplateCreate,
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    admin_required(user)
    template_obj = crud.create_template(db, template)
    return schemas.Template.from_orm(template_obj)


@router.put("/", response_model=schemas.Template)
async def update_template(
    template_id: str, template: schemas.TemplateCreate,
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    admin_required(user)
    template_obj = crud.update_template(db, template, template_id)
    return schemas.Template.from_orm(template_obj)


@router.delete("/", response_model=schemas.GenericMessage)
async def update_template(
    template_id: str,
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    admin_required(user)
    template_obj = crud.delete_template(db, template_id)
    return schemas.GenericMessage(message="Template deleted successfully!")

