from flask import Flask, render_template

app = Flask(__name__)

"""
Задание №1
Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!".
"""


@app.route("/")
def index():
    return "Hello, world!"


"""
Задание №2
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше вебприложение:
○ страницу "about"
○ страницу "contact".
"""


@app.route("/about/")
def about():
    return "Info about us"


@app.route("/contact/")
def contact():
    return "Contacts info"


"""
Задание №3
Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.
"""


@app.route("/numbers/<int:num1>/<int:num2>/")
def sum_numbers(num1, num2):
    return f"Сумма чисел {num1} и {num2} равна {num1 + num2}"


"""
Задание №4
Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
"""


@app.route("/len/<string>/")
def len_string(string):
    return f'Длина строки "{string}" = {len(string)} '


"""
Задание №5
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".
"""


html = """
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>"""


@app.route("/page/")
def first_html_page():
    return html


"""
Задание №6
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст.
"""


@app.route("/students/")
def students():
    _students = [
        {"name": "Иван", "second_name": "Иванов", "age": 20, "average_score": 4.6},
        {"name": "Степан", "second_name": "Лавров", "age": 21, "average_score": 4.2},
        {"name": "Александр", "second_name": "Попов", "age": 24, "average_score": 3.9},
    ]
    context = {"title": "Список студентов", "students": _students}
    return render_template("students.html", **context)


"""
Задание №7
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""


@app.route("/news/")
def news():
    _news = [
        {
            "title": "Молния",
            "text": "Люди увидели молнию",
            "pub_date": "01.01.1900",
        },
        {
            "title": "Праздники в мае",
            "text": "В мае отмеают 1 мая - день труда и 9 мая - день ПОБЕДЫ",
            "pub_date": "21.01.2024",
        },
        {
            "title": "Ром - кола",
            "text": "Состав: ром кола в соотношении 1 к 4, добавить лёд",
            "pub_date": "01.12.2023",
        },
    ]
    context = {"title": "Новости", "news": _news}
    return render_template("news.html", **context)


"""
Задание №8
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""


@app.route("/about_us/")
def about_us():
    context = {"title": "О нас"}
    return render_template("about.html", **context)


@app.route("/contacts/")
def contacts():
    context = {"title": "Контакты"}
    return render_template("contacts.html", **context)


if __name__ == "__main__":
    app.run()
