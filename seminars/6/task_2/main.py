"""
Задание №2
Создать веб-приложение на FastAPI, которое будет предоставлять API для
работы с базой данных пользователей. Пользователь должен иметь
следующие поля:
○ ID (автоматически генерируется при создании пользователя)
○ Имя (строка, не менее 2 символов)
○ Фамилия (строка, не менее 2 символов)
○ Дата рождения (строка в формате "YYYY-MM-DD")
○ Email (строка, валидный email)
○ Адрес (строка, не менее 5 символов)
API должен поддерживать следующие операции:
○ Добавление пользователя в базу данных
○ Получение списка всех пользователей в базе данных
○ Получение пользователя по ID
○ Обновление пользователя по ID
○ Удаление пользователя по ID
Приложение должно использовать базу данных SQLite3 для хранения
пользователей.

"""

import uvicorn
from users_routers import router as users_routers
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
app.include_router(users_routers, tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
