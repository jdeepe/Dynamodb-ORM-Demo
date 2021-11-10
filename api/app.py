from flask import Flask
from flask_cors import CORS

from api import health
from api.dataset import schema_views
from api.dataset import views as dataset_views


def create_app(config_object):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    cors = CORS()
    origins = app.config.get("CORS_ORIGIN_WHITELIST", "*")
    cors.init_app(health.blueprint, origins=origins)
    app.register_blueprint(health.blueprint, url_prefix="/")

    cors.init_app(dataset_views.blueprint, origins=origins)
    app.register_blueprint(dataset_views.blueprint, url_prefix="/v1/dataset")

    cors.init_app(schema_views.blueprint, origins=origins)
    app.register_blueprint(schema_views.blueprint, url_prefix="/v1/dataschema")
