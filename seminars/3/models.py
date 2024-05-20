from typing import Any
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.relationships import RelationshipProperty

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(7), nullable=False)
    group =db.Column(db.String(30), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    # students = db.relationship('Faculty', backref='studs', lazy=True)
    def __repr__(self) -> str:
        return f'Student: {self.name} {self.surname}, group: {self.group}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self) -> str:
        return self.title
    
