import datetime
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_6 import RegisterForm
"""
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




if __name__ == "__main__":
    app.run(debug=True)
