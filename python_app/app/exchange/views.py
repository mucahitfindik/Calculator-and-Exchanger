from flask import Blueprint, request
from app.riksbank.riksbank import Riksbank
import datetime as dt

blueprint = Blueprint('exchange', __name__)


@blueprint.route('/currency-list', methods=('GET',))
def get_currency_list():
    return {'currency_list': Riksbank.get_currency_list()}


@blueprint.route('/exchange', methods=('POST',))
def get_exchanged_result():

    data = request.get_json()
    if "amount" not in data or data["amount"] == "":
        return {'result': "No amount provided!"}
    elif "toCurrency" not in data or data["toCurrency"] == "":
        return {'result': "No toCurrency provided!"}
    elif "fromCurrency" not in data or data["fromCurrency"] == "":
        return {'result': "No fromCurrency provided!"}

    amount = data["amount"]
    to_currency = data["toCurrency"]
    from_currency = data["fromCurrency"]
    date = dt.date.fromisoformat(data["date"])
    if not isinstance(to_currency, list):
        to_currency = [to_currency]
    if from_currency not in Riksbank.get_currency_list():
        return {'result': "Currency list doesn't include " + from_currency}

    for currency in to_currency:
        if currency not in Riksbank.get_currency_list():
            return {'result': "Currency list doesn't include " + currency}

    return Riksbank.exchange_currency(amount, to_currency, from_currency, date)
