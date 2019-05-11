from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Обязательное поле!'),
            Email(message='Неправильный Email адрес!')
        ])
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired(message='Обязательное поле!')
        ])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
