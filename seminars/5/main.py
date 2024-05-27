import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
Задание №1
Создать API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа
"""


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool


tasks = []


@app.get("/")
async def index():
    return {"title": "Seminar 5"}


@app.get("/tasks/", response_model=list[Task])
async def get_task():
    return tasks


@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    if [t for t in tasks if t.id == task.id]:
        return {"message_error": "This id is already in use"}
    tasks.append(task)
    logger.info(f'Task id={task.id} {task.title} - успешно добавлен')
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    for num in range(len(tasks)):
        if tasks[num].id == task_id:
            tasks[num] = task
            logger.info(f'Task id={task.id} - успешно изменен')
            return tasks[num]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            logger.info(f'Task id={task.id} {task.title} - успешно удален')
            return {"message": f"Task id={task_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
