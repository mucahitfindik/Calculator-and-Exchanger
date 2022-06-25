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
    def exchange_currency(cls, to_currency, from_currency, date):
        cross_rate = get_cross_rate(to_currency, from_currency, date)
        return cross_rate
