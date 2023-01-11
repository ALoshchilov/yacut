from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .messages import SHORT_NOT_FOUND
from .models import URLMap
from .utils import generate_unique_short_id
from .api_validators import (
    validate_custom_short, validate_original_url, validate_request
)


@app.route('/api/id/', methods=['POST'])
def add_url_map():
    data = validate_request(request.get_json())
    original = validate_original_url(data.get('url'))
    custom_short = validate_custom_short(data.get('custom_id'))
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


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify({'url': url.original})
    raise InvalidAPIUsage(SHORT_NOT_FOUND, 404)
