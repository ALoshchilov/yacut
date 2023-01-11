from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .models import URLMap


SHORT_REGEXP = r'^[a-zA-Z\d]{1,16}$'

class UrlCutForm(FlaskForm):
    url = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Проверьте правильность написания ссылки!')
        ]
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки",
        validators=[
            Optional(),
            Length(1, 16, message= 'Допустимая длина пользовательского варианта короткой ссылки от 1 до 16'),
            Regexp(
                regex=SHORT_REGEXP,
                message='Ссылка может содержать только цифры и буквы "a-Z"!')]
    )

    # def validate_short(self):
    # Число символов в кате 6, нет такой ссылки
    #     return 
