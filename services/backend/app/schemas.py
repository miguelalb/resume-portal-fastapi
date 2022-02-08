from typing import Any, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel


# Shared Properties
class UserBase(BaseModel):
    username: str


# Properties to receive on create
class UserCreate(UserBase):
    password: str


# Properties in DB
class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True
