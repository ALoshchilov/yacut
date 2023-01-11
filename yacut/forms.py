from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .models import URLMap
from .settings import CUSTOM_SHORT_MAX_LENGTH, CUSTOM_SHORT_MIN_LENGTH


SHORT_REGEXP = r'^[a-zA-Z\d]{1,16}$'

class UrlCutForm(FlaskForm):
    url = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Проверьте правильность написания ссылки!')
        ]
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Optional(),
            Length(
                CUSTOM_SHORT_MIN_LENGTH,
                CUSTOM_SHORT_MAX_LENGTH,
                message=f'Допустимая длина пользовательского варианта короткой ссылки от {CUSTOM_SHORT_MIN_LENGTH} до {CUSTOM_SHORT_MAX_LENGTH}'),
            Regexp(
                regex=SHORT_REGEXP,
                message='Ссылка может содержать только цифры и буквы "a-Z"!')]
    )
    submit = SubmitField('Создать')
