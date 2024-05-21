from flask import Flask, render_template
from models_2 import db, Author, Book


app = Flask(__name__)


"""
Задание №2
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
"""

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
db.init_app(app)


# Инициируем базу данных
@app.cli.command("init-db")
def init_db():
    db.create_all()


# Добавляем авторов
@app.cli.command("fill-autors")
def fill_authors_db():
    authors = [
        ["Александр", "Пушкин"],
        ["Лев", "Толстой"],
        ["Максим", "Горький"],
        ["Михайло", "Ломоносов"],
    ]
    # Если фамилии автора нет в библиотеке, добавляем нового автора
    for author in authors:
        lib_author = Author.query.filter_by(surname=author[1]).first()
        if not lib_author:
            auth = Author(name=author[0], surname=author[1])
            db.session.add(auth)
    db.session.commit()


# Добавляем книги
@app.cli.command("fill-books")
def fill_books_db():
    for i in range(1, 5):
        counter = 1
        while counter <= 5:
            book = Book(
                name=f"Book{counter}", pub_year=1900, copy=counter + 1, author_id=i
            )
            db.session.add(book)
            counter += 1
    db.session.commit()


# Показываем книги в библиотеке
@app.cli.command("show")
def show_library():
    library = Book.query.all()
    print(*[book for book in library], sep="\n")


# if __name__ == "__main__":
#     app.run(debug=True)
