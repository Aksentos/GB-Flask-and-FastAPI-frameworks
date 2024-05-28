import uvicorn
import logging
from typing import Annotated
from fastapi import FastAPI, HTTPException, Request, Form
from pydantic import BaseModel, EmailStr, constr
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Чтобы использовать формы, сначала установите python-multipart.
# Например, выполните команду pip install python-multipart.

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
Задание №6
Создать веб-страницу для отображения списка пользователей. Приложение
должно использовать шаблонизатор Jinja для динамического формирования HTML
страницы.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
содержать заголовок страницы, таблицу со списком пользователей и кнопку для
добавления нового пользователя.
Создайте маршрут для отображения списка пользователей (метод GET).
Реализуйте вывод списка пользователей через шаблонизатор Jinja.
"""
# нужно указать полный путь до папки templates
templates = Jinja2Templates(directory="templates")


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
@app.get("/users/", response_class=HTMLResponse)
async def all_users(request: Request):
    global users
    context = {"request": request, "title": "Список пользователей", "users": users}
    return templates.TemplateResponse("users.html", context)


# маршрут для добавления нового пользователя
@app.post("/users/")
async def create_user(
    request: Request,
    id: Annotated[int, Form()],
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    if email not in [user.email for user in users]:
        users.append(User(id=id, name=name, email=email, password=password))
        logger.info(f"{name} registered")
        return templates.TemplateResponse(
            "users.html", {"request": request, "users": users}
        )
    raise HTTPException(403, detail=f"User with email={email} is already registered")


if __name__ == "__main__":
    uvicorn.run("task_6:app", host="localhost", port=8000, reload=True)
