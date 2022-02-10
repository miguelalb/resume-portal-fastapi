import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from app.database import Base


class BaseMixin(object):
    """ Shared properties and common functionality """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, index=True)

class TimestampMixin(object):
    created_at = Column(String, default=datetime.now().timestamp())

class CurrentMixin(object):
    current = Column(Boolean, default=False)


class DeletedMixin(object):
    deleted = Column(Boolean, default=False, nullable=True)


class User(Base, BaseMixin, TimestampMixin):
    username = Column(String, index=True)
    password = Column(String, index=True)

    profile = relationship(
        "UserProfile", cascade="all,delete",
        back_populates="user", uselist=False)

    def __str__(self):
        return f"<User: {self.username}>"


class UserProfile(Base, BaseMixin, TimestampMixin):
    first_name = Column(String)
    last_name = Column(String)
    public_name = Column(String)
    theme = Column(String)
    summary = Column(String)
    email = Column(String)
    phone = Column(String)
    designation = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))

    user = relationship("User", back_populates="profile")
    skills = relationship("Skill", cascade="all,delete",
        back_populates="profile", lazy="joined")
    jobs = relationship("Job", cascade="all,delete",
        back_populates="profile", lazy="joined")
    educations = relationship("Education", cascade="all,delete",
        back_populates="profile", lazy="joined")
    certifications = relationship("Certification", cascade="all,delete",
        back_populates="profile", lazy="joined")


    def __str__(self):
        return f"<Profile: {self.first_name} {self.last_name}>"


class Skill(Base, BaseMixin, DeletedMixin):
    name = Column(String, index=True)
    learning = Column(Boolean, default=False)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('userprofile.id'))

    profile = relationship("UserProfile", back_populates="skills")

    def __str__(self):
        return f"<Skill: {self.name}>"

class Job(Base, BaseMixin, CurrentMixin, DeletedMixin):
    company = Column(String, index=True)
    designation = Column(String, index=True)
    description = Column(Text)
    startdate = Column(String)
    enddate = Column(String, nullable=True)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('userprofile.id'))

    profile = relationship("UserProfile", back_populates="jobs")

    def __str__(self):
        return f"<Job: {self.company}>"


class Education(Base, BaseMixin, CurrentMixin, DeletedMixin):
    college = Column(String, index=True)
    designation = Column(String)
    description = Column(Text)
    startdate = Column(String)
    enddate = Column(String, nullable=True)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('userprofile.id'))

    profile = relationship("UserProfile", back_populates="educations")

    def __str__(self):
        return f"<Education: {self.college}>"

class Certification(Base, BaseMixin, CurrentMixin, DeletedMixin):
    name = Column(String, index=True)
    issuing_organization = Column(String)
    issue_date = Column(String)
    expiration_date = Column(String, nullable=True)
    credential_id = Column(String, nullable=True)
    credential_url = Column(String, nullable=True)
    profile_id = Column(UUID(as_uuid=True), ForeignKey('userprofile.id'))

    profile = relationship("UserProfile", back_populates="certifications")

    def __str__(self):
        return f"<Certification: {self.name}>"
