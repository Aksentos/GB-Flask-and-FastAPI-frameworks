from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field(..., title="Title", max_length=50)
    description: str = Field(..., title="description", max_length=120)
    status: bool = Field(..., title="Status")


class Task(TaskIn):
    id: int
