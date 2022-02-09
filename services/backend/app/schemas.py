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


class SkillCreate(SkillBase):
    pass


class JobCreate(JobBase):
    pass


class EducationCreate(EducationBase):
    pass


class CertificationCreate(CertificationBase):
    pass


class UserProfileCreate(UserProfileBase):
    skills: Optional[List[SkillCreate]] = []
    jobs: Optional[List[JobCreate]] = []
    educations: Optional[List[EducationCreate]] = []
    certifications: Optional[List[CertificationCreate]] = []


# Properties on Update
class UserUpdate(UserCreate):
    pass


# Properties in DB
class User(UserBase):
    id = UUID

    class Config:
        orm_mode = True


class Skill(SkillBase):
    id = UUID

    class Config:
        orm_mode = True


class Job(JobBase):
    id = UUID

    class Config:
        orm_mode = True


class Education(EducationBase):
    id = UUID

    class Config:
        orm_mode = True


class Certification(CertificationBase):
    id = UUID

    class Config:
        orm_mode = True


class UserProfile(UserProfileBase):
    id = UUID
    skills: Optional[List[Skill]] = []
    jobs: Optional[List[Job]] = []
    educations: Optional[List[Education]] = []
    certifications: Optional[List[Certification]] = []

    class Config:
        orm_mode = True
