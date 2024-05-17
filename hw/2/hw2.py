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
from multiprocessing import context
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    name = request.cookies.get("username")
    if name:
        context = {"name": name}
        response = make_response(render_template('index.html'), **context)
        return response
        
    return redirect(url_for('log_in'))

@app.route('/login/', methods=["GET", "POST"])
def log_in():
    context = {"title": "Страница входа"}
    if request.method == "POST":
        name = request.form.get("name")
        mail = request.form.get("mail")
        response = make_response(render_template('index.html'))
        response.set_cookie("username", name)
        response.set_cookie("username", mail)
        return redirect(url_for('index'))
                           
    return render_template("login.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
