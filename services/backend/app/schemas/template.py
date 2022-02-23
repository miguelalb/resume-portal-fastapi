from app.schemas.base import IDOptionalMixin, ORMModeMixin
from pydantic import BaseModel


# shared properties
class TemplateBase(BaseModel):
    name: str
    content: str
    premium: bool


# properties on Create
class TemplateCreate(TemplateBase):
    pass


# properties on Update
class TemplateUpdate(TemplateCreate, IDOptionalMixin):
    pass


# properties in DB
class Template(TemplateBase, ORMModeMixin):
    pass
