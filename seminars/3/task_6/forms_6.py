from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Optional

# для отработки валидации Email, необходимо утсановить: pip install email-validator


