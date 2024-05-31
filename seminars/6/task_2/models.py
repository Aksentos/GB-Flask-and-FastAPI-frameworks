from datetime import date
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int
    name: str = Field(..., title="Name", max_length=20)
    surname: str = Field(..., title="surname", max_length=20)
    birthday: date = Field(...,  title="Birthday", description="YYYY-MM-DD")
    email: EmailStr = Field(..., title="Email", max_length=128)
    address: str = Field(title="Address", max_length=128)


class UserIn(BaseModel):
    name: str = Field(..., title="Name", max_length=20)
    surname: str = Field(..., title="surname", max_length=20)
    birthday: date = Field(...,  title="Birthday", description="YYYY-MM-DD")
    email: EmailStr = Field(..., title="Email", max_length=128)
    address: str = Field(title="Address", max_length=128)
