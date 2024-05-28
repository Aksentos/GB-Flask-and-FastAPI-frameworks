import uvicorn
import logging
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
Задание №2
Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: str


# список movies для хранения фильмов
movies = [
    Movie(id=1, title="Titanic", description="Oscar film", genre="drama"),
    Movie(id=2, title="1+1", description="Top comedy", genre="comedy"),
    Movie(
        id=3,
        title="Sinister",
        description="The house turns out to be a terrible trap",
        genre="horror",
    ),
    Movie(
        id=4,
        title="Romanovs",
        description="The history of the Romanov House",
        genre="dokumentary",
    ),
    Movie(
        id=5,
        title="Zootopia",
        description="Welcome to the urban jungle",
        genre="cartoon",
    ),
    Movie(
        id=6,
        title="Sherlock",
        description="The best detective of the 21st century",
        genre="detective",
    ),
]


@app.get("/")
async def index():
    return {"title": "Seminar 5"}


#  маршрут для получения списка всех жанров
@app.get("/all_genres/")
async def all_genres():
    return [movie.genre for movie in movies]


#  маршрут для получения списка всех фильмов
@app.get("/movies/", response_model=list[Movie])
async def all_movies():
    return movies


#  маршрут для получения списка фильмов по жанру
@app.get("/movie/{genre}")
async def find_movie(genre: str):
    users_movies = [mov for mov in movies if genre == mov.genre]
    if users_movies:
        return users_movies
    raise HTTPException(status_code=404, detail=f"Movie with genre={genre} not found")


if __name__ == "__main__":
    uvicorn.run("task_2:app", host="localhost", port=8000, reload=True)
