from flask import Flask, render_template
from models_3 import db, Student, Grade
from random import randint

app = Flask(__name__)


"""
Задание №3
Доработаем задача про студентов
Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
База данных должна содержать две таблицы: "Студенты" и "Оценки".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
Необходимо создать связь между таблицами "Студенты" и "Оценки".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
"""

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.db"
db.init_app(app)


# Инициируем базу данных
@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем студентов
    for i in range(1, 4):
        new_student = Student(
            name=f"Иван{i}",
            surname=f"Иванов{i}",
            group="gr-1",
            email=f"mail{i}@example.com",
        )
        db.session.add(new_student)
    db.session.commit()

    # Добавляем преметы
    lessons = ["Математика", "Ин.яз"]
    for lesson in lessons:
        students = Student.query.all()
        for i in range(1, len(students) + 1):
            less = Grade(lesson=lesson, mark=randint(2, 5), student_id=i)
            db.session.add(less)
    db.session.commit()


@app.cli.command("show")
def show_students_grades():
    students = Student.query.all()
    print(*[student for student in students], sep="\n")


# if __name__ == "__main__":
#     app.run(debug=True)
