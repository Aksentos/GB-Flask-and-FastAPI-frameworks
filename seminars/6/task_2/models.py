from datetime import date
from pydantic import BaseModel, EmailStr, Field




class UserIn(BaseModel):
    name: str = Field(..., title="Name", min_length=2)
    surname: str = Field(..., title="surname", min_length=2)
    birthday: date = Field(..., title="Birthday", description="YYYY-MM-DD")
    email: EmailStr = Field(..., title="Email", max_length=128)
    address: str = Field(title="Address", min_length=5, max_length=128)

class User(UserIn):
    id: int
