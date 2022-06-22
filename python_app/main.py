from flask.helpers import get_env

from app.app import create_app
from app.config import DevConfig, ProdConfig
CONFIG = DevConfig if get_env() == 'development' else ProdConfig
app = create_app(CONFIG)
