from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)


class UserData(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=3, max_length=50)
