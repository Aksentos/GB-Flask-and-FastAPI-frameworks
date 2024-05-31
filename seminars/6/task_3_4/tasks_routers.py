import logging
from fastapi import APIRouter, HTTPException
from models import Task, TaskIn
from db import db, tasks
from typing import List



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


task_router = APIRouter()


@task_router.get("/tasks/", response_model=List[Task])
async def get_tasks():
    query = tasks.select()
    return await db.fetch_all(query)


@task_router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    existing_task = await db.fetch_one(query)
    if existing_task:
        query = tasks.select().where(tasks.c.id == task_id)
        return await db.fetch_one(query)
    raise HTTPException(status_code=404, detail="Task not found")


@task_router.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.model_dump())
    last_id = await db.execute(query)
    logger.info(f"Task = {task} added")
    return {**task.model_dump(), "id": last_id}


@task_router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.select().where(tasks.c.id == task_id)
    existing_task = await db.fetch_one(query)
    if existing_task:
        query = (
            tasks.update().where(tasks.c.id == task_id).values(**new_task.model_dump())
        )
        await db.execute(query)
        logger.info(f"Task id={task_id} changed")
        return {**new_task.model_dump(), "id": task_id}
    raise HTTPException(status_code=404, detail="Task not found")


@task_router.delete("/tasks/{task_id}")
async def delete_user(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    existing_task = await db.fetch_one(query)
    if existing_task:
        query = tasks.delete().where(tasks.c.id == task_id)
        await db.execute(query)
        logger.info(f"Task id={task_id} deleted")
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
