from typing import Any, List, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel


# Security
class Token(BaseModel):
    access_token: str
    token_type: str

# Shared Properties
class UserBase(BaseModel):
    username: str


class UserProfileBase(BaseModel):
    first_name: str
    last_name: str
    public_name: str
    theme: str
    summary: str
    email: str
    phone: str
    designation: str


class SkillBase(BaseModel):
    name: str
    learning: bool


class JobBase(BaseModel):
    company: str
    designation: str
    description: str
    startdate: str
    current: bool
    enddate: Optional[str] = None

class EducationBase(BaseModel):
    college: str
    designation: str
    description: str
    startdate: str
    current: bool
    enddate: Optional[str] = None


class CertificationBase(BaseModel):
    name: str
    issuing_organization: str
    issue_date: str
    current: bool
    expiration_date: Optional[str] = None
    credential_id: Optional[str] = None
    credential_url: Optional[AnyUrl] = None


# Properties on Create
class UserCreate(UserBase):
    password: str


class UserProfileCreate(UserProfileBase):
    pass


# Properties on Update
class UserUpdate(UserCreate):
    pass


# Properties in DB
class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True
