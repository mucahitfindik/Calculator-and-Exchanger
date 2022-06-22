# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
from app import exchange
from app.config import ProdConfig
from flask_cors import CORS


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors_ = CORS()
    cors_.init_app(exchange.views.blueprint, origins=origins)

    app.register_blueprint(exchange.views.blueprint)
    return app

"""
from flask import Flask

app = Flask(__name__)

print(__name__)
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5002, debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
