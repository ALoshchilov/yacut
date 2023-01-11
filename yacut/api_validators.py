import re

from .error_handlers import InvalidAPIUsage
from .messages import (
    BODY_MISSING, REQUIRED_FIELD_MISSING, SHORT_ALREADY_EXIST,
    WRONG_ORIGINAL_URL_MESSAGE, WRONG_SHORT_NAME_MESSAGE
)
from .settings import (
    CUSTOM_SHORT_MAX_LENGTH, CUSTOM_SHORT_MIN_LENGTH, SHORT_REGEXP, URL_REGEXP
)
from .utils import is_short_unique


def validate_request(data):
    if not(type(data) is dict or bool(data)):
        raise InvalidAPIUsage(BODY_MISSING)
    return data


def validate_custom_short(short):
    if short is None or short == "":
        return None
    if not CUSTOM_SHORT_MIN_LENGTH <= len(short) <= CUSTOM_SHORT_MAX_LENGTH:
        raise InvalidAPIUsage(WRONG_SHORT_NAME_MESSAGE)
    if not re.match(SHORT_REGEXP, short):
        raise InvalidAPIUsage(WRONG_SHORT_NAME_MESSAGE)
    if not is_short_unique(short):
        raise InvalidAPIUsage(SHORT_ALREADY_EXIST.format(short=short))
    return short


def validate_original_url(original):
    if not original:
        raise InvalidAPIUsage(REQUIRED_FIELD_MISSING)
    if re.match(
        re.compile(URL_REGEXP, re.IGNORECASE),
        original
    ) is None:
        raise InvalidAPIUsage(WRONG_ORIGINAL_URL_MESSAGE)
    return original
