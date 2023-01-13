from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .messages import BODY_MISSING, COMMON_SERVER_ERROR, SHORT_NOT_FOUND
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_url_map():
    data = request.get_json()
    if not(type(data) is dict or bool(data)):
        raise InvalidAPIUsage(BODY_MISSING)
    try:
        return jsonify(
            URLMap.create_in_db(
                original=URLMap.validate_original(data.get('url')),
                short=URLMap.validate_short(data.get('custom_id')),
            ).to_dict()
        ), 201
    except (AssertionError, ValueError) as error:
        raise InvalidAPIUsage(str(error))
    except Exception as error:
        raise InvalidAPIUsage(
            COMMON_SERVER_ERROR.format(error=str(error)),
            500
        )


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    url = URLMap.get_url_map(short=short_id)
    if url is not None:
        return jsonify({'url': url.original})
    raise InvalidAPIUsage(SHORT_NOT_FOUND, 404)
