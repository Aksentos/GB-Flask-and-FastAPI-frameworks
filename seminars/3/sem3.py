from flask import Flask, render_template
from models import db, Student, Faculty


app = Flask(__name__)

"""
Задание №1
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
db.init_app(app)


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем факультеты
    faculties = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    for faculty in faculties:
        new_fac = Faculty(title=faculty)
        db.session.add(new_fac)
    db.session.commit()

    # Добавляем студентов
    for i in range(1, len(faculties) + 1):
        for j in range(1, 5):
            new_student = Student(
                name=f"Garry{j}",
                surname=f"Potter{j}",
                age=11,
                gender="male",
                group="gr-1",
                faculty_id=i,
            )
            db.session.add(new_student)
    db.session.commit()


# проверка связи факультета со студентами
@app.cli.command("fff")
def fff():
    griff = Faculty.query.filter_by(title="Gryffindor").first()
    print(griff.students)


# проверка связи студентов с факультетами
@app.cli.command("sss")
def fff():
    studs = Student.query.filter_by(name="Garry1").all()
    for s in studs:
        print(s.faculty)


# if __name__ == "__main__":
#     app.run(debug=True)
