import datetime
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_5 import RegisterForm
"""
Задание №5
Создать форму регистрации для пользователя.
Форма должна содержать поля: имя, электронная почта,
пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
Валидация должна проверять, что все поля заполнены
корректно (например, дата рождения должна быть в
формате дд.мм.гггг).
При успешной регистрации пользователь должен быть
перенаправлен на страницу подтверждения регистрации
"""


app = Flask(__name__)

app.config["SECRET_KEY"] = (
    "90cd8c67244a3eaa20f5b49cf19285e11de4b52f00400dddac1ecda9b776832b"
)
csrf = CSRFProtect((app))


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/registration/", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        birthday = form.birthday.data
        birthday = f'{birthday.day}.{birthday.month}.{birthday.year}'

        context = {
            'title': "Форма регистрации",
            "username": username,
            "email": email,
            "password": password,
            "birthday": birthday,
        }
        return render_template('index.html', **context)
    # не забываем добавить форму на страничку
    return render_template("registration.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
