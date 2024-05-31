from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: int
    username: str = Field(..., title="Name", max_length=10)
    email: EmailStr = Field(..., title="Email")
    password: str = Field(..., title="Password", min_length=4)


class UserIn(BaseModel):
    username: str = Field(..., title="Name", max_length=10)
    email: EmailStr = Field(..., title="Email")
    password: str = Field(..., title="Password", min_length=4)
