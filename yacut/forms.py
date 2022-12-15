from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms.validators import DataRequired

from .models import URLMap

class UrlCutForm(FlaskForm):
    original = URLField(
        "Длинная ссылка",
        validators=[DataRequired(message='Обязательное поле')]
    )
    short = URLField(
        "Ваш вариант короткой ссылки"
    )

    # def validate_short(self):
    # Число символов в кате 6, нет такой ссылки
    #     return 
