from flask import Blueprint, request

blueprint = Blueprint('exchange', __name__)


@blueprint.route('/exchange', methods=('GET',))
def get_articles():
    data = request.get_json()
    if "amount" not in data or data["amount"] == "":
        return {'result': "No amount provided!"}
    elif "toCurrency" not in data or data["toCurrency"] == "":
        return {'result': "No toCurrency provided!"}
    elif "fromCurrency" not in data or data["fromCurrency"] == "":
        return {'result': "No fromCurrency provided!"}

    amount = data["amount"]
    toCurrency = data["toCurrency"]
    fromCurrency = data["fromCurrency"]
    return {'result': "Hello World!"}
