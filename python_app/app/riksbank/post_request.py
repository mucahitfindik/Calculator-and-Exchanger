import requests
from app.functions import parse_all_cross_names_response, parse_get_cross_rate
from app.riksbank.soap.configure_soap import ConfigureSoap

url = "http://swea.riksbank.se/sweaWS/services/SweaWebServiceHttpSoap12Endpoint"


def all_cross_names():
    body, headers = ConfigureSoap.soap_all_cross_names()
    response = requests.post(url, data=body, headers=headers)
    return parse_all_cross_names_response(response.content)


def get_cross_rate(to_currency, from_currency, date):
    body, headers = ConfigureSoap.soap_cross_rates(to_currency, from_currency, date)
    response = requests.post(url, data=body, headers=headers)
    cross_rate = parse_get_cross_rate(response.content, to_currency, from_currency)
    if cross_rate == -1:
        return get_cross_rate(to_currency, from_currency, date.replace(day=(date.day - 1)))
    return cross_rate
