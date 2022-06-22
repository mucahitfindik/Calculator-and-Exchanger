from flask import Blueprint

blueprint = Blueprint('exchange', __name__)


@blueprint.route('/exchange', methods=('GET',))
def get_articles():
    return "Hello World!"
