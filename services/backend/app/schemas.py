from typing import Any, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel


# Security
class Token(BaseModel):
    access_token: str
    token_type: str

# Shared Properties
class UserBase(BaseModel):
    username: str


# Properties on Create
class UserCreate(UserBase):
    password: str


# Properties on Update
class UserUpdate(UserCreate):
    pass


# Properties in DB
class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True
