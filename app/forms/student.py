from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email, NumberRange


class StudentForm(FlaskForm):
    name = StringField(
        'Имя',
        validators=[
            DataRequired(message='Обязательное поле!')
        ])
    age = DecimalField(
        'Возраст',
        validators=[
            DataRequired(message='Обязательное поле!'),
            NumberRange(min=0, max=120,
                        message='Возраст должен быть больше 0 и меньше 121!')
        ])
    address = StringField(
        'Адрес',
        validators=[
            DataRequired(message='Обязательное поле!')
        ])
    submit = SubmitField('Создать')
