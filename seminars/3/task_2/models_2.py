from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
Задача 2
"""


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pub_year = db.Column(db.Integer, nullable=False)
    copy = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    def __repr__(self) -> str:
        return f'"{self.name}", автор -  {self.author}, год издания - {self.pub_year}, количество копий - {self.copy}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), unique=True, nullable=False)
    books = db.relationship("Book", backref="author", lazy=True)

    def __repr__(self) -> str:
        return self.surname
