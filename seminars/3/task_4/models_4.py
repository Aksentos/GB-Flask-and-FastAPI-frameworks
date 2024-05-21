from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
Задача 4
"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"Username: {self.name}, Mail: {self.email}"
