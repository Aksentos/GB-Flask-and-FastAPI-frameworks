from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

# для отработки валидации Email, необходимо утсановить: pip install email-validator


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    birthday = DateField("Birthday", format="%Y-%m-%d", validators=[Optional()])
    confirm = BooleanField(
        "Согласие на обработку персональный данных", validators=[DataRequired()]
    )
