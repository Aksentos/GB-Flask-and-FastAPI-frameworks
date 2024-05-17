"""
Задание №9
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import (
    Flask,
    render_template,
    request,
    make_response,
    redirect,
    url_for,
)

app = Flask(__name__)
app.secret_key = "816b422c25127e8a51af86a65e2821b3c23bc6407baa64f37281382b503b204a"


@app.route("/")
@app.route("/index/")
def index():
    name = request.cookies.get("username")
    print(f"index - {name}")
    if name:
        context = {"name": name}
        response = make_response(render_template("index.html", **context))
        return response

    return redirect(url_for("login"))


@app.route("/login/", methods=["GET", "POST"])
def login():
    context = {"title": "Страница входа"}
    if request.method == "POST":
        name = request.form.get("name")
        mail = request.form.get("mail")
        context["name"] = name
        response = make_response(render_template("index.html", **context))
        response.set_cookie("username", name)
        response.set_cookie("usermail", mail)
        return response
    response = make_response(render_template("login.html"))
    response.delete_cookie("username")
    response.delete_cookie("usermail")
    return response


if __name__ == "__main__":
    app.run(debug=True)
