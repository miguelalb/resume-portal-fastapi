from pydantic import BaseModel


# Security
class Token(BaseModel):
    access_token: str
    token_type: str
