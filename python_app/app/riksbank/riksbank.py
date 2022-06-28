from app.riksbank.postRequest import all_cross_names, get_cross_rate
from flask import json, Response


class Riksbank:
    __currency_dict = {}

    @classmethod
    def get_currency_list(cls):
        if Riksbank.__currency_dict == {}:
            Riksbank.__currency_dict = all_cross_names()
        return Riksbank.__currency_dict

    @classmethod
    def exchange_currency(cls, amount, to_currency, from_currency, date):
        response = []
        for currency in to_currency:
            cross_rate = get_cross_rate(currency, from_currency, date)
            response.append({'result': amount * cross_rate, 'to_currency': currency, 'cross_rate': cross_rate})
        res = Response(json.dumps(response), mimetype="application/json", status=200)
        return res
