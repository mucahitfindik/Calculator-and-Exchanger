from flask import Blueprint, request,jsonify
from app.riksbank.riksbank import Riksbank
from app.validator.exchange.post_request import InvalidRequestParameter, InvalidCurrency, check_required_parameters, \
    check_currency_supported
import datetime as dt

blueprint = Blueprint('exchange', __name__)


@blueprint.errorhandler(400)
def invalid_request(e):
    return jsonify({"error": 'The body of this request is unexpected.'}), 400


@blueprint.route('/currency-list', methods=('GET',))
def get_currency_list():
    return jsonify({'currency_list': Riksbank.get_currency_list()}), 200


@blueprint.route('/exchange', methods=('POST',))
def get_exchanged_result():

    data = request.get_json()
    print(type(data))

    try:
        check_required_parameters(data)
    except InvalidRequestParameter as err:
        return jsonify({"error": err.message}), 404

    amount = data["amount"]
    to_currency = data["toCurrency"]
    from_currency = data["fromCurrency"]
    date = dt.date.fromisoformat(data["date"])
    currency_list = Riksbank.get_currency_list()

    if not isinstance(to_currency, list):
        to_currency = [to_currency]

    try:
        check_currency_supported(from_currency, to_currency, currency_list)
    except InvalidCurrency as err:
        return jsonify({"error": err.message}), 404

    return jsonify(Riksbank.exchange_currency(amount, to_currency, from_currency, date)), 200
