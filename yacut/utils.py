from random import choice

from .error_handlers import InvalidAPIUsage
from .messages import NO_AVAILABLE_SHORTS
from .models import URLMap
from .settings import MAX_GENERATION_BAD_ATTEMPS, MAX_SHORT_LENGTH, SHORT_ALLOWED_SYMBOLS


def is_original_in_db(original):
    url_map = URLMap.query.filter_by(original=original).first()
    if url_map:
        return url_map
    return None

def is_short_unique(short):
    if URLMap.query.filter_by(short=short).first():
        return False
    return True

def generate_random_short(lenght=MAX_SHORT_LENGTH,):
    return "".join([choice(SHORT_ALLOWED_SYMBOLS) for _ in range(lenght)])

def generate_unique_short_id(
        max_bad_attemps=MAX_GENERATION_BAD_ATTEMPS
    ):
    short = generate_random_short()
    bad_attemps = 0
    while not is_short_unique(short):
        short = generate_random_short()
        bad_attemps += 1
        if bad_attemps == max_bad_attemps:
            raise InvalidAPIUsage(NO_AVAILABLE_SHORTS, 500)
    return short
