from typing import Optional

from app import crud, schemas
from app.dependencies import get_db, get_user
from app.exceptions import Exc
from app.security import decode_access_token
from app.utils import render_template
from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/{public_name}", response_model=schemas.UserProfileRender)
async def get_profile_by_public_name(public_name: str, db: Session = Depends(get_db)):
    user_profile = crud.get_user_profile_by_public_name(db, public_name)
    if user_profile is None:
        raise Exc.ObjectNotFoundException("User Profile")
    # TODO Complete jinja2 render. This should return the decoded HTML
    # template = render_template(template_content, data)
    return schemas.UserProfile.from_orm(user_profile)


@router.get("/me", response_model=schemas.UserProfile)
async def get_profile_me(user=Depends(get_user), db: Session = Depends(get_db)):
    profile_obj = crud.get_user_profile_by_id(db, user.profile_id)
    return schemas.UserProfile.from_orm(profile_obj)


@router.post(
    "", response_model=schemas.UserProfile, status_code=status.HTTP_201_CREATED
)
async def create_profile(
    user_profile: schemas.UserProfileCreate,
    user=Depends(get_user),
    db: Session = Depends(get_db),
):

    user_profile_obj = crud.create_user_profile(db, user_profile, user.id)
    return schemas.UserProfile.from_orm(user_profile_obj)


@router.put("/{profile_id}", response_model=schemas.UserProfile)
async def update_profile(
    profile_id: str,
    user_profile: schemas.UserProfileUpdate,
    token: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    user = decode_access_token(db, token)
    updated_profile = crud.update_user_profile(db, user_profile, profile_id, user.id)
    return schemas.UserProfile.from_orm(updated_profile)


@router.delete("/{profile_id}", response_model=schemas.GenericMessage)
async def delete_profile(
    profile_id: str, token: Optional[str] = Header(None), db: Session = Depends(get_db)
):
    crud.delete_user_profile(db, profile_id)
    return schemas.GenericMessage(message="Profile deleted successfully")
