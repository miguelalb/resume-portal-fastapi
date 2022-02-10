from typing import Any, List, Optional, Union
from uuid import UUID

from pydantic import AnyUrl, BaseModel


# Security
class Token(BaseModel):
    access_token: str
    token_type: str


# Shared Base Properties and Mixins
class IDOptionalMixin(BaseModel):
    id: Optional[UUID] = None

class ORMModeMixin(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class DeletedMixin(BaseModel):
    deleted: Optional[bool] = None


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


class SkillUpdate(SkillBase, IDOptionalMixin, DeletedMixin):
    pass


class JobUpdate(JobBase, IDOptionalMixin, DeletedMixin):
    pass


class EducationUpdate(EducationBase, IDOptionalMixin, DeletedMixin):
    pass


class CertificationUpdate(CertificationBase, IDOptionalMixin, DeletedMixin):
    pass


class UserProfileUpdate(UserProfileBase, IDOptionalMixin):
    skills: Optional[List[SkillUpdate]] = []
    jobs: Optional[List[JobUpdate]] = []
    educations: Optional[List[EducationUpdate]] = []
    certifications: Optional[List[CertificationUpdate]] = []


# Properties in DB
class User(UserBase, ORMModeMixin):
    pass


class Skill(SkillBase, ORMModeMixin):
    pass


class Job(JobBase, ORMModeMixin):
    pass


class Education(EducationBase, ORMModeMixin):
    pass


class Certification(CertificationBase, ORMModeMixin):
    pass


class UserProfile(UserProfileBase, ORMModeMixin):
    skills: Optional[List[Skill]] = []
    jobs: Optional[List[Job]] = []
    educations: Optional[List[Education]] = []
    certifications: Optional[List[Certification]] = []
