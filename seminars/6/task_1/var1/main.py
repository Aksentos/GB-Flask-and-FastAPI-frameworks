"""
Задание №1
Разработать API для управления списком пользователей с
использованием базы данных SQLite. Для этого создайте
модель User со следующими полями:
○ id: int (идентификатор пользователя, генерируется
автоматически)
○ username: str (имя пользователя)
○ email: str (электронная почта пользователя)
○ password: str (пароль пользователя)
API должно поддерживать следующие операции:
○ Получение списка всех пользователей: GET /users/
○ Получение информации о конкретном пользователе: GET /users/{user_id}/
○ Создание нового пользователя: POST /users/
○ Обновление информации о пользователе: PUT /users/{user_id}/
○ Удаление пользователя: DELETE /users/{user_id}/
Для валидации данных используйте параметры Field модели User.
Для работы с базой данных используйте SQLAlchemy и модуль databases.
"""

import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from models import User, UserIn, metadata, db, engine, users
from typing import List
from werkzeug.security import generate_password_hash


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

metadata.create_all(engine)

app = FastAPI()


@app.get("/users/", response_model=List[User])
async def get_users():
    query = users.select()
    return await db.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def get_users(user_id: int):
    query = users.select().where(users.c.id == user_id)
    existing_user = await db.fetch_one(query)
    if existing_user:
        query = users.select().where(users.c.id == user_id)
        return await db.fetch_one(query)
    raise HTTPException(status_code=404, detail="User not found")


# получить выборку из таблицы
@app.get("/users_skip/", response_model=List[User])
async def get_limit_users(skip: int = 0, limit: int = 5):
    query = users.select().offset(skip).limit(limit)
    return await db.fetch_all(query)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    password = generate_password_hash(user.password)
    query = users.insert().values(
        username=user.username, email=user.email, password=password
    )
    last_id = await db.execute(query)
    logger.info(f"User = {user} added")
    return {**user.model_dump(), "id": last_id}


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.select().where(users.c.id == user_id)
    existing_user = await db.fetch_one(query)
    if existing_user:
        password = generate_password_hash(new_user.password)
        query = (
            users.update()
            .where(users.c.id == user_id)
            .values(username=new_user.username, email=new_user.email, password=password)
        )
        await db.execute(query)
        logger.info(f"User id={user_id} changed")
        return {**new_user.model_dump(), "id": user_id}
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int, new_user: UserIn):
    query = users.select().where(users.c.id == user_id)
    existing_user = await db.fetch_one(query)
    if existing_user:
        query = users.delete().where(users.c.id == user_id)
        await db.execute(query)
        logger.info(f"User id={user_id} deleted")
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)