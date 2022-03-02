from typing import List, Optional
from uuid import UUID

from app.schemas.base import (DeletedMixin, IDOptionalMixin, ORMModeMixin,
                              PrettifyDatesMixin)
from app.schemas.template import Template
from pydantic import AnyUrl, BaseModel


# shared properties
class UserProfileBase(BaseModel):
    first_name: str
    last_name: str
    public_name: str
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


class UserProfileRender(BaseModel):
    content: str


# properties on Create
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
    template_id: UUID


# properties on Update
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
    template_id: UUID


# properties in DB
class Skill(SkillBase, ORMModeMixin):
    pass


class Job(JobBase, ORMModeMixin):
    pass


class JobPrettyDate(Job, PrettifyDatesMixin):
    pass


class Education(EducationBase, ORMModeMixin):
    pass


class EducationPrettyDate(Education, PrettifyDatesMixin):
    pass


class Certification(CertificationBase, ORMModeMixin):
    pass


class CertificationPrettyDate(Certification, PrettifyDatesMixin):
    pass


class UserProfile(UserProfileBase, ORMModeMixin):
    skills: Optional[List[Skill]] = []
    jobs: Optional[List[Job]] = []
    educations: Optional[List[Education]] = []
    certifications: Optional[List[Certification]] = []
    template: Optional[Template] = None


class UserProfilePrettyDate(UserProfileBase, ORMModeMixin):
    skills: Optional[List[Skill]] = []
    jobs: Optional[List[JobPrettyDate]] = []
    educations: Optional[List[EducationPrettyDate]] = []
    certifications: Optional[List[CertificationPrettyDate]] = []
    template: Optional[Template] = None
