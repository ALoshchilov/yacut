import re
from datetime import datetime
from random import sample
from urllib.parse import urlparse

from flask import url_for

from . import db
from .error_handlers import MaxGenerationAttemptsExceeded
from .messages import (
    NO_AVAILABLE_SHORTS, ORIGINAL_TOO_LONG, REQUIRED_FIELD_MISSING,
    SHORT_ALREADY_EXIST, WRONG_ORIGINAL_URL_MESSAGE, WRONG_SHORT_NAME_MESSAGE
)
from .settings import (
    CUSTOM_SHORT_MAX_LENGTH, MAX_GENERATION_BAD_ATTEMPS, MAX_SHORT_LENGTH,
    ORIGINAL_MAX_URL_LENGTH, SHORT_ALLOWED_SYMBOLS, SHORT_REGEXP
)
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_MAX_URL_LENGTH), nullable=False)
    short = db.Column(db.String(MAX_SHORT_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        self.original = data['url'],
        self.short = data['short_link']

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_to_original',
                short_id=self.short,
                _external=True
            )
        )

    @staticmethod
    def validate_original(original):
        if not original:
            raise ValueError(REQUIRED_FIELD_MISSING)
        if len(original) > ORIGINAL_MAX_URL_LENGTH:
            raise ValueError(ORIGINAL_TOO_LONG)
        parsed_url = urlparse(original)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError(WRONG_ORIGINAL_URL_MESSAGE)
        return original

    @staticmethod
    def validate_short(short):
        if short is None or short == "":
            return None
        if len(short) > CUSTOM_SHORT_MAX_LENGTH:
            raise ValueError(WRONG_SHORT_NAME_MESSAGE)
        if not re.match(SHORT_REGEXP, short):
            raise ValueError(WRONG_SHORT_NAME_MESSAGE)
        return short

    @staticmethod
    def generate_random_short(length=MAX_SHORT_LENGTH,):
        return "".join(sample(SHORT_ALLOWED_SYMBOLS, length))

    @staticmethod
    def get_url_map(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_url_map_or_404(short):
        return URLMap.query.filter_by(short=short).first_or_404()

    @staticmethod
    def create_in_db(original, short=None):
        if short is None or short == "":
            short = URLMap.generate_unique_short_id()
        url_map = URLMap.get_url_map(short)
        if url_map:
            raise ValueError(
                SHORT_ALREADY_EXIST.format(short=url_map.short)
            )
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def generate_unique_short_id(
        max_bad_attemps=MAX_GENERATION_BAD_ATTEMPS
    ):
        for _ in range(max_bad_attemps):
            short = URLMap.generate_random_short()
            if not URLMap.get_url_map(short):
                return short
        raise MaxGenerationAttemptsExceeded(NO_AVAILABLE_SHORTS)
