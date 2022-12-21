from datetime import datetime
from enum import unique

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2048), nullable=False)
    # MAX FQDN - 253 знака, https:// - 8 знаков, /abCD01 - 7 знаков
    # Итого 268
    short = db.Column(db.String(268), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
