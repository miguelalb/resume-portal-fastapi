from datetime import datetime
from typing import Optional
from uuid import UUID

from app.utils import prettify_timestamp
from pydantic import BaseModel, validator


# Shared Base Properties and Mixins
class IDOptionalMixin(BaseModel):
    id: Optional[UUID] = None


class ORMModeMixin(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class DeletedMixin(BaseModel):
    deleted: Optional[bool] = None


class PrettifyDatesMixin(BaseModel):
    @validator('startdate', check_fields=False)
    def convert_startdate(cls, value):
        if value not in ["", None]:
            return prettify_timestamp(value)
        return value

    @validator('enddate', check_fields=False)
    def convert_enddate(cls, value):
        if value not in ["", None]:
            return prettify_timestamp(value)
        return value
    
    @validator('issue_date', check_fields=False)
    def convert_issuedate(cls, value):
        if value not in ["", None]:
            return prettify_timestamp(value)
        return value

    @validator('expiration_date', check_fields=False)
    def convert_expiration_date(cls, value):
        if value not in ["", None]:
            return prettify_timestamp(value)
        return value
