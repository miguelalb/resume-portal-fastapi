from pydantic import BaseModel


class GenericMessage(BaseModel):
    message: str
