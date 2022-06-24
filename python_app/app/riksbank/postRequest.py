import requests
from app.functions import parse_all_cross_names_response, parse_get_cross_rate
from app.riksbank.soap.configure_soap import ConfigureSoap

url = "http://swea.riksbank.se/sweaWS/services/SweaWebServiceHttpSoap12Endpoint"


def all_cross_names():
    body, headers = ConfigureSoap.soap_all_cross_names()
    response = requests.post(url, data=body, headers=headers)
    return parse_all_cross_names_response(response.content)


def get_cross_rate(to_currency, from_currency):
    body, headers = ConfigureSoap.soap_cross_rates(to_currency, from_currency)
    response = requests.post(url, data=body, headers=headers)
    return parse_get_cross_rate(response.content, to_currency, from_currency)

