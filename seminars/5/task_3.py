import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
Задание №3
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.
"""


class User(BaseModel):
    id: int
    name: str
    email: EmailStr  # валидация email
    password: constr(min_length=4, max_length=10)  # валидация пароля по кол-ву символов


# список users для хранения пользователей
users = []


@app.get("/")
async def index():
    return {"title": "Главня страница"}


# маршрут для отображения всех пользователей
@app.get("/users/", response_model=list[User])
async def all_users():
    return users


# маршрут для добавления нового пользователя
@app.post("/user/", response_model=User)
async def create_user(user: User):
    if user.id not in [u.id for u in users]:
        users.append(user)
        logger.info(f"{user.name} registered")
        return user
    raise HTTPException(403, detail=f"User with id={user.id} is already registered")


if __name__ == "__main__":
    uvicorn.run("task_3:app", host="localhost", port=8000, reload=True)
