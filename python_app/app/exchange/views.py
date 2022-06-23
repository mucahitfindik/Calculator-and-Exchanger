from flask import Blueprint, request

blueprint = Blueprint('exchange', __name__)


@blueprint.route('/exchange', methods=('GET',))
def get_articles():
    data = request.get_json()
    amount = data["amount"]
    toCurrency = data["toCurrency"]
    fromCurrency = data["fromCurrency"]
    return "Hello World!"
