from os import abort
import re
from unittest import result
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
        if file_name.endswith(("jpg", "jpeg", "png")):
            file.save(PurePath.joinpath(Path.cwd(), "static/images", file_name))
            return f"Картинка {file_name} загружена на сервер"

    return render_template("upload.html", title="Загрузка картинки на сервер")


"""
Задание №3
Создать страницу, на которой будет форма для ввода логина и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""

USERS = {"Alex": "1234", "Admin": "1111"}


@app.route("/login/", methods=["GET", "POST"])
def login():
    context = {"message": None, "url": request.base_url}

    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        if name in USERS:
            if USERS[name] == password:
                return render_template("hello.html", name=name)
            context["message"] = f"Неверный пароль"
            return render_template("404.html", **context), 404
        context["message"] = f"Пользователь с таким именем не зарегистрирован"
        return render_template("404.html", **context), 404
    return render_template("login.html", title="Страница входа")


@app.errorhandler(404)
def page_not_found(e):
    context = {
        "title": "Страница не найдена",
        "url": request.base_url,
    }
    return render_template("404.html", **context), 404


"""
Задание №4
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""


@app.route("/input_text/", methods=["GET", "POST"])
def input_text():
    context = {
        "title": "Страничка для ввода текста",
    }
    if request.method == "POST":
        text = request.form.get("text_area")
        context["title"] = "Информация о тексте"
        context["count_words"] = len(text.split())
        context["count_chars"] = len(text)
        return render_template("text_info.html", **context)
    return render_template("input_text.html", **context)


"""
Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""


@app.route("/calculate/", methods=["GET", "POST"])
def calculate():
    context = {
        "title": "Калькулятор",
    }
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")
        if operation in ("+", "-", "*", "/"):
            result = eval(num1 + operation + num2)
            context["num1"] = num1
            context["num2"] = num2
            context["operation"] = operation
            context["result"] = result
            return render_template("calculate.html", **context)
    return render_template("calculate.html", **context)


"""
Задание №6
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""


@app.route("/age/", methods=["GET", "POST"])
def age_verification():
    context = {
        "title": "Проверка возраста",
    }
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        if age.isdigit():
            if int(age) < 18:
                context["message"] = "Вам еще нет 18 лет!"
                return render_template("403.html", **context), 403
            else:
                context["name"] = name
                return render_template("hello.html", **context)
    return render_template("age.html", **context)


"""
Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""


@app.route("/squaring/", methods=["GET", "POST"])
def squaring():
    context = {
        "title": "Возведение числа в квадрат",
    }
    if request.method == "POST":
        num3 = request.form.get("num3")
        try:
            num = float(num3)
            result = num**2
            context["num3"] = num3
            context["result"] = result
            print("tyt")
            return render_template("squaring.html", **context)
        except:
            pass  # error 405
    return render_template("squaring.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
