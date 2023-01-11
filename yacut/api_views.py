from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .messages import REQUIRED_FIELD_MISSING, SHORT_ALREADY_EXIST, SHORT_NOT_FOUND
from .models import URLMap
from .utils import generate_unique_short_id, is_original_in_db, is_short_unique


@app.route('/api/id/', methods = ['POST'])
def add_url_map():
    data = request.get_json()
    original = data.get('url')
    if not original:
        raise InvalidAPIUsage(REQUIRED_FIELD_MISSING.format(field='url'))
    custom_short  = data.get('custom_id')
    if custom_short and not is_short_unique(custom_short):
        raise InvalidAPIUsage(SHORT_ALREADY_EXIST, 400)
    url_map = is_original_in_db(original)
    if url_map and custom_short is None:
        return jsonify(url_map.to_dict()), 200
    short = generate_unique_short_id()
    url_map = URLMap(
        original=original,
        short=custom_short or short
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        url_map.to_dict()
    ), 201

@app.route('/api/id/<short_id>/', methods = ['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(id=short_id).first()
    # url = URLMap.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify({'url': url.original})
    raise InvalidAPIUsage(SHORT_NOT_FOUND, 404)
