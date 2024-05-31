"""
Задание №3
Создать API для управления списком задач.
Каждая задача должна содержать поля "название",
"описание" и "статус" (выполнена/не выполнена).
API должен позволять выполнять CRUD операции с
задачами.

Задание №4
Напишите API для управления списком задач. Для этого создайте модель Task
со следующими полями:
○ id: int (первичный ключ)
○ title: str (название задачи)
○ description: str (описание задачи)
○ done: bool (статус выполнения задачи)
API должно поддерживать следующие операции:
○ Получение списка всех задач: GET /tasks/
○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
○ Создание новой задачи: POST /tasks/
○ Обновление информации о задаче: PUT /tasks/{task_id}/
○ Удаление задачи: DELETE /tasks/{task_id}/
Для валидации данных используйте параметры Field модели Task.
Для работы с базой данных используйте SQLAlchemy и модуль databases.

"""

import uvicorn
from tasks_routers import task_router 
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import db


# Вместо @app.on_event нужно использовать lifespan!
@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


# Создем объект FastAPI с lifespan
app = FastAPI(lifespan=lifespan)

# Регистрируем роутеры
app.include_router(task_router, tags=["tasks"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
