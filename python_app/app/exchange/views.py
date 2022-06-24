from flask import Blueprint, request
from app.riksbank.riksbank import Riksbank


blueprint = Blueprint('exchange', __name__)


@blueprint.route('/currency-list', methods=('GET',))
def get_currency_list():
    return Riksbank.get_currency_list()


@blueprint.route('/exchange', methods=('GET',))
def get_articles():

    data = request.get_json()
    if "amount" not in data or data["amount"] == "":
        return {'result': "No amount provided!"}
    elif "toCurrency" not in data or data["toCurrency"] == "":
        return {'result': "No toCurrency provided!"}
    elif "fromCurrency" not in data or data["fromCurrency"] == "":
        return {'result': "No fromCurrency provided!"}
    elif not data["toCurrency"] in Riksbank.get_currency_list():
        return {'result': "Currency list doesn't include" + data["toCurrency"]}
    elif not data["fromCurrency"] in Riksbank.get_currency_list():
        return {'result': "Currency list doesn't include" + data["fromCurrency"]}
    amount = data["amount"]
    to_currency = data["toCurrency"]
    from_currency = data["fromCurrency"]

    return Riksbank.exchange_currency(amount, to_currency, from_currency)
