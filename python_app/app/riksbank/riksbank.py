from app.riksbank.postRequest import all_cross_names, get_cross_rate
import datetime as dt


class Riksbank:
    __currency_dict = {}

    @classmethod
    def get_currency_list(cls):
        if Riksbank.__currency_dict == {}:
            Riksbank.__currency_dict = all_cross_names()
        return Riksbank.__currency_dict

    @classmethod
    def exchange_currency(cls, amount, to_currency, from_currency):
        cross_rate = get_cross_rate(to_currency, from_currency, dt.datetime.now().date())
        return {'result': amount*cross_rate}
