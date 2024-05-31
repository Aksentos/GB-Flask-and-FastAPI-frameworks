"""
Необходимо создать базу данных для интернет-магазина. 
База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, 
их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, 
сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию 
о зарегистрированных пользователях магазина.
• Таблица пользователей должна содержать следующие поля: 
id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: 
id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: 
id (PRIMARY KEY), название, описание и цена.

Создайте модели pydantic для получения новых данных и возврата существующих в БД 
для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.
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
