from app.schemas.base import ORMModeMixin
from pydantic import BaseModel


# shared properties
class UserBase(BaseModel):
    username: str


# properties on Create
class UserCreate(UserBase):
    password: str


class UserLogin(UserCreate):
    pass

# properties on Update
class UserUpdate(UserCreate):
    pass


# properties in DB
class User(UserBase, ORMModeMixin):
    is_admin: bool
    is_premium: bool
