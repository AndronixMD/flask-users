from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email, NumberRange


class StudentForm(FlaskForm):
    name = StringField(
        'Email',
        validators=[
            DataRequired(message='Обязательное поле!'),
            Email(message='Неправильный Email адрес!')
        ])
    age = DecimalField(
        'Возраст',
        validators=[
            DataRequired(message='Обязательное поле!'),
            NumberRange(min=0, max=120,
                        message='Возраст должен быть больше 0 и меньше 121!')
        ])
    address = StringField(
        'Пароль',
        validators=[
            DataRequired(message='Обязательное поле!')
        ])
    submit = SubmitField('Создать')
