from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
Задача 3
"""


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    group = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    grades = db.relationship("Grade", backref="student", lazy=True)

    def __repr__(self) -> str:
        return f"Student: {self.name} {self.surname}, оценки: {self.grades}"


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson = db.Column(db.String(50), nullable=False)
    mark = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))

    def __repr__(self) -> str:
        return f"{self.lesson}, оценка: {self.mark}"
