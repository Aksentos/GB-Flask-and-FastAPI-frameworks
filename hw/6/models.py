from pydantic import BaseModel, EmailStr, Field


class UserIn(BaseModel):
    name: str = Field(..., title="Name", max_length=50)
    surname: str = Field(..., title="Surname", max_length=50)
    email: EmailStr = Field(..., title="Email", max_length=50)
    password: str = Field(..., title="Password")


class User(UserIn):
    id: int
