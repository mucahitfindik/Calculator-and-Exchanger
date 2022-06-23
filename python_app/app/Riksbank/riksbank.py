from app.Riksbank.postRequest import all_cross_names


class Riksbank:

    __currency_dict = {}

    @classmethod
    def get_currency_list(cls):
        if Riksbank.__currency_dict == {}:
            Riksbank.__currency_dict = all_cross_names()
        return Riksbank.__currency_dict
