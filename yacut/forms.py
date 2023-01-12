from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (
    DataRequired, Length, Optional, Regexp, URL, ValidationError
)

from .messages import (
    CHECK_URL_MESSAGE, CREATE_BUTTON_TEXT, ORIGINAL_URL_FORM_DESCRIPTION,
    ORIGINAL_TOO_LONG, REQUIRED_FIELD_MESSAGE, SHORT_ALREADY_EXIST_FORM,
    SHORT_FORM_DESCRIPTION, WRONG_SHORT_NAME_MESSAGE
)
from .models import URLMap
from .settings import CUSTOM_SHORT_MAX_LENGTH, SHORT_REGEXP, ORIGINAL_MAX_URL_LENGTH


class UrlCutForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_URL_FORM_DESCRIPTION,
        validators=[
            DataRequired(message=REQUIRED_FIELD_MESSAGE),
            URL(message=CHECK_URL_MESSAGE),
            Length(
                max=ORIGINAL_MAX_URL_LENGTH,
                message=ORIGINAL_TOO_LONG
            ),
        ]
    )
    custom_id = StringField(
        SHORT_FORM_DESCRIPTION,
        validators=[
            Optional(),
            Length(
                max=CUSTOM_SHORT_MAX_LENGTH,
                message=WRONG_SHORT_NAME_MESSAGE
            ),
            Regexp(
                regex=SHORT_REGEXP,
                message=WRONG_SHORT_NAME_MESSAGE
            )
        ]
    )
    submit = SubmitField(CREATE_BUTTON_TEXT)

    def validate_custom_id(self, field):
        if field.data and URLMap.get_url_map(field.data):
            raise ValidationError(
                SHORT_ALREADY_EXIST_FORM.format(short=field.data)
            )
