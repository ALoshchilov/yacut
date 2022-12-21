from random import choice
from string import ascii_letters, digits

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .messages import NO_AVAILABLE_SHORTS, REQUIRED_FIELD_MISSING, SHORT_ALREADY_EXIST, SHORT_NOT_FOUND
from .models import URLMap
from .settings import BASE_URL, MAX_GENERATION_BAD_ATTEMPS, MAX_SHORT_LENGTH


def generate_unique_short_id(
        lenght=MAX_SHORT_LENGTH,
        max_bad_attemps=MAX_GENERATION_BAD_ATTEMPS
    ):
    short = "".join([choice(ascii_letters + digits) for _ in range(lenght)])
    bad_attemps = 0
    while URLMap.query.filter_by(short=short).first() is not None:
        short = "".join([choice(ascii_letters + digits) for _ in range(lenght)])
        bad_attemps += 1
        if bad_attemps == max_bad_attemps:
            raise InvalidAPIUsage(NO_AVAILABLE_SHORTS, 500)
    return short

@app.route('/api/id/', methods = ['POST'])
def add_url_map():
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_FIELD_MISSING.format(field='url'))
    if 'custom_id' in data and URLMap.query.filter_by(short=data.get('custom_id')).first() is not None:
        raise InvalidAPIUsage(SHORT_ALREADY_EXIST, 400)
    url_map = URLMap(
        original=data.get('url'),
        short=data.get('custom_id', generate_unique_short_id())
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        {'url': url_map.original, 'short_link': f'{BASE_URL}/{url_map.short}'}
    ), 201

@app.route('/api/id/<short_id>/', methods = ['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify({'url': url.original})
    raise InvalidAPIUsage(SHORT_NOT_FOUND, 404)
