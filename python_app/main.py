from flask.helpers import get_env
from flask import jsonify

from app.app import create_app
from app.config import DevConfig, ProdConfig
CONFIG = DevConfig if get_env() == 'development' else ProdConfig
app = create_app(CONFIG)


@app.errorhandler(404)
def invalid_route(e):
    """
    Error handler for unexpected endpoint

    """
    return jsonify({"error": 'The requested URL was not found on the server.'}), 404


@app.errorhandler(405)
def invalid_method(e):
    """
    Error handler for unexpected endpoint

    """
    return jsonify({"error": 'The method is not allowed for the requested URL.'}), 405
