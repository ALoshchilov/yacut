from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (
    DataRequired, Length, Optional, Regexp, URL, ValidationError
)

from .messages import (
    CHECK_URL_MESSAGE, REQUIRED_FIELD_MESSAGE, SHORT_ALREADY_EXIST_FORM,
    WRONG_SHORT_NAME_MESSAGE
)
from .settings import (
    CUSTOM_SHORT_MAX_LENGTH, CUSTOM_SHORT_MIN_LENGTH, SHORT_REGEXP
)
from .utils import is_short_unique


class UrlCutForm(FlaskForm):
    original_link = URLField(
        "Длинная ссылка",
        validators=[
            DataRequired(message=REQUIRED_FIELD_MESSAGE),
            URL(message=CHECK_URL_MESSAGE)
        ]
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Optional(),
            Length(
                CUSTOM_SHORT_MIN_LENGTH,
                CUSTOM_SHORT_MAX_LENGTH,
                message=WRONG_SHORT_NAME_MESSAGE
            ),
            Regexp(
                regex=SHORT_REGEXP,
                message=WRONG_SHORT_NAME_MESSAGE
            )
        ]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if field.data and not is_short_unique(field.data):
            raise ValidationError(
                SHORT_ALREADY_EXIST_FORM.format(short=field.data)
            )
