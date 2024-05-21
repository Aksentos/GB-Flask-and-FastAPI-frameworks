from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from models_4 import db, User
from forms_4 import LoginForm


app = Flask(__name__)


"""
Задание №4
Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.
"""


app.config["SECRET_KEY"] = (
    "07d6cc02fe88d96b996d9c81094c090e07ad6e4f7645fb633d4978c4ffff7da1"
)
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db.init_app(app)


# Инициируем базу данных
@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        #  Проверяем на уникальность email в бд, если такого нет добавляем в БД
        user = User.query.filter_by(email=email).first()
        if not user:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template("index.html", username=username)
        # если такаой мэйл уже есть, то вызываем сообщение
        flash("Пользователь с такой почтой уже зарегистрирован", "warning")
        return redirect(url_for("register"))

    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
