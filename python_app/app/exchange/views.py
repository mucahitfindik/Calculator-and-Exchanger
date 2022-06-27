from flask import Blueprint, request
from app.riksbank.riksbank import Riksbank
import datetime as dt

blueprint = Blueprint('exchange', __name__)


@blueprint.route('/currency-list', methods=('GET',))
def get_currency_list():
    return Riksbank.get_currency_list()


@blueprint.route('/exchange', methods=('GET',))
def get_exchanged_result():

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
    date = dt.date.fromisoformat(data["date"])
    cross_rate = Riksbank.exchange_currency(to_currency, from_currency, date)
    return {'result': amount*cross_rate, 'cross_rate': cross_rate}
