import xmltodict


def parse_all_cross_names_response(content):
    content_d = xmltodict.parse(content)
    content_d = content_d["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["ns0:getAllCrossNamesResponse"]["return"]
    cross_names = {}
    for item in content_d:
        cross_names[item["seriesname"]["#text"]] = item["seriesdescription"]["#text"]
    return cross_names


def parse_get_cross_rate(content, to_currency, from_currency):
    content_d = xmltodict.parse(content)
    content_d = content_d["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["ns0:getCrossRatesResponse"]["return"]
    if "groups" not in content_d:
        return -1
    content_d = content_d["groups"]["series"]
    for item in content_d:
        if item["seriesname"]["#text"] == '1 '+from_currency+' = ? '+to_currency:
            return float(item["resultrows"]["value"]['#text'])
