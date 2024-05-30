import databases
import sqlalchemy as sql
from pydantic import BaseModel, EmailStr, Field

DATABASE_URL = "sqlite:///task_1/users.db"

db = databases.Database(DATABASE_URL)
engine = sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata = sql.MetaData()


users = sql.Table(
    "users",
    metadata,
    sql.Column("id", sql.Integer, primary_key=True),
    sql.Column("username", sql.String(10)),
    sql.Column("email", sql.String(20)),
    sql.Column("password", sql.String(10)),
)


class User(BaseModel):
    id: int
    username: str = Field(..., title="Name", max_length=10)
    email: EmailStr = Field(..., title="Email")
    password: str = Field(..., title="Password", min_length=4)


class UserIn(BaseModel):
    username: str = Field(..., title="Name", max_length=10)
    email: EmailStr = Field(..., title="Email")
    password: str = Field(..., title="Password", min_length=4)
