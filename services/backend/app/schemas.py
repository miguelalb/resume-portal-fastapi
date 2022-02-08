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


# Properties to receive on create
class UserCreate(UserBase):
    password: str


# Properties in DB
class User(UserBase):
    id: UUID

    class Config:
        orm_mode = True
