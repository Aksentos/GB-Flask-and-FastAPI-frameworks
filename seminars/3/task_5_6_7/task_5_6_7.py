import string
from flask import Flask, render_template, request, flash, redirect, url_for
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

Задание №6
Дополняем прошлую задачу
Создайте форму для регистрации пользователей в вашем
веб-приложении.
Форма должна содержать следующие поля: имя
пользователя, электронная почта, пароль и подтверждение
пароля.
Все поля обязательны для заполнения, и электронная почта
должна быть валидным адресом.
После отправки формы, выведите успешное сообщение об
успешной регистрации.

Задание №7
Создайте форму регистрации пользователей в приложении Flask. Форма должна
содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
формы данные должны валидироваться на следующие условия:
○ Все поля обязательны для заполнения.
○ Поле email должно быть валидным email адресом.
○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
одну цифру.
○ Поле подтверждения пароля должно совпадать с полем пароля.
○ Если данные формы не прошли валидацию, на странице должна быть выведена
соответствующая ошибка.
○ Если данные формы прошли валидацию, на странице должно быть выведено
сообщение об успешной регистрации.
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

        # Состоит ли строка из цифр или букв
        if not any(char.isdigit() for char in password) or not any(
            char.isalpha() for char in password
        ):

            flash("Пароль должен состоять из букв и цифр", "warning")
            return redirect(url_for("registration"))

        birthday = form.birthday.data
        birthday = f"{birthday.day}.{birthday.month}.{birthday.year}"

        context = {
            "title": "Форма регистрации",
            "username": username,
            "email": email,
            "password": password,
            "birthday": birthday,
        }
        return render_template("index.html", **context)
    # не забываем добавить форму на страничку
    return render_template("registration.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
