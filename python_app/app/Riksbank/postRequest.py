from jinja2 import Environment, PackageLoader
import requests
from app.functions import parse_all_corse_names_response

url = "http://swea.riksbank.se/sweaWS/services/SweaWebServiceHttpSoap12Endpoint"
headers = {'content-type': 'application/soap+xml'}


def all_cross_names():
    headers['action'] = 'urn:getAllCrossNames'
    env = Environment(loader=PackageLoader('app', 'templates'))
    template = env.get_template('soaprequests/AllCrosNames.xml')
    body = template.render()
    response = requests.post(url, data=body, headers=headers)
    return parse_all_corse_names_response(response.content)
