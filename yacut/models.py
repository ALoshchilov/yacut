from datetime import datetime

from .settings import BASE_URL
from yacut import db


URLMAP_AS_DICT_FIELDS ={
    'original': 'url',
    'short': 'custom_id'
}

class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2048), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        for db_field, form_field in URLMAP_AS_DICT_FIELDS.items():
            if form_field in data:
                setattr(self, db_field, data[form_field])

    def to_dict(self):
        urlmap_dict = {}
        for db_field in URLMAP_AS_DICT_FIELDS:
            if db_field == 'short':
                urlmap_dict[db_field] = f'{BASE_URL}/{str(getattr(self, db_field))}'
                continue
            urlmap_dict[db_field] = f'{str(getattr(self, db_field))}'
        return urlmap_dict
