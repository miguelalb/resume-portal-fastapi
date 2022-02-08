from app import crud
from app.dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{public_name}")
async def get_profile_by_public_name(public_name: str, db: Session = Depends(get_db)):
    return "Ok - Profile by Public Name"
