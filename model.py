from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3, max_length=50)


class User(UserIn):
    id: int
