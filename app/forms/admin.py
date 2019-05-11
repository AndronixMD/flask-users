from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models.user import User


class AdminForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[
            DataRequired(message='Обязательное поле!')
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Обязательное поле!'),
            Email(message='Неправильный Email адрес!')
        ])
    type_user = SelectField(
        'Тип пользователя',
        choices=[('admin', 'Админ'), ('teacher', 'Учитель')],
        validators=[
            DataRequired('Обязательное поле!')
        ])
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired(message='Обязательное поле!')
        ])
    password2 = PasswordField(
        'Повторить пароль',
        validators=[
            DataRequired(message='Обязательное поле!'),
            EqualTo('password')
        ])
    submit = SubmitField('Создать')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Этот email уже занят!')
