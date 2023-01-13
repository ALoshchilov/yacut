from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_sqlalchemy import SQLAlchemy
from settings import Config


app = Flask(__name__)
app.config.from_object(Config)
api = swagger.docs(Api(app), apiVersion='1', api_spec_url="/api/v1/spec")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
