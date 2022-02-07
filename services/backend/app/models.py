import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from app.database import Base


class BaseMixin(object):
    """ Shared properties and common functionality"""
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    id = Column(
        UUID(as_uuid=True), primary_key=True,
        default=uuid.uuid4, index=True)

class TimestampMixin(object):
    created_at = Column(String, default=datetime.now().timestamp())


class User(Base, BaseMixin, TimestampMixin):
    username = Column(String, index=True)
    password = Column(String, index=True)

    profile = relationship("UserProfile", cascade="all,delete", back_populates="user")

    def __str__(self):
        return f"<User: {self.username}>"


class UserProfile(Base, BaseMixin, TimestampMixin):
    first_name = Column(String)
    last_name = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))

    user = relationship("User", back_populates="profile")
