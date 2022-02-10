from typing import Optional

from app import crud, schemas
from app.dependencies import get_db
from app.exceptions import Exc
from app.security import decode_access_token
from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{public_name}", response_model=schemas.UserProfile)
async def get_profile_by_public_name(public_name: str, db: Session = Depends(get_db)):
    user_profile = crud.get_user_profile_by_public_name(db, public_name)
    if user_profile is None:
        raise Exc.ProfileNotFoundException
    return schemas.UserProfile.from_orm(user_profile)


@router.post("/", response_model=schemas.UserProfile)
async def create_profile(
    user_profile: schemas.UserProfileCreate,
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    user_profile_obj = crud.create_user_profile(db, user_profile, user.id)
    return schemas.UserProfile.from_orm(user_profile_obj)

@router.put("/", response_model=schemas.UserProfile)
async def update_profile(
    user_profile: schemas.UserProfileUpdate,
    token: Optional[str] = Header(None), db: Session = Depends(get_db)):
    user = decode_access_token(db, token)
    updated_profile = crud.update_user_profile(db, user_profile, user.id)
    return schemas.UserProfile.from_orm(updated_profile)
