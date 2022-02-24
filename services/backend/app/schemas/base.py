from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared Base Properties and Mixins
class IDOptionalMixin(BaseModel):
    id: Optional[UUID] = None


class ORMModeMixin(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class DeletedMixin(BaseModel):
    deleted: Optional[bool] = None
