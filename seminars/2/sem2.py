from flask import Flask, render_template, request, url_for

app = Flask(__name__)

"""
Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/name/", methods=["GET", "POST"])
def hello_form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Привет {name}"
    return render_template("name_form.html", title="Как тебя зовут?")


"""
Задание №2
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path


@app.route("/image/")
def image():
    context = {"title": "Картинка", "image": "/static/images/1.jpg"}
    return render_template("image.html", **context)


@app.route("/upload/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        file = request.files.get("file")
        file_name = secure_filename(file.filename)
        if file_name.endswith(('jpg', 'jpeg', 'png')):
            file.save(PurePath.joinpath(Path.cwd(), "static/images", file_name))
            return f"Картинка {file_name} загружена на сервер"

    return render_template("upload.html", title="Загрузка картинки на сервер")


'''
Задание №3
Создать страницу, на которой будет форма для ввода логина и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
'''
from 









if __name__ == "__main__":
    app.run(debug=True)
