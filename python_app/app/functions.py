import xmltodict


def parse_all_cross_names_response(content):
    content_d = xmltodict.parse(content)
    content_d = content_d["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["ns0:getAllCrossNamesResponse"]["return"]
    cross_names = {}
    for item in content_d:
        cross_names[item["seriesname"]["#text"]] = item["seriesdescription"]["#text"]
    return cross_names


def parse_get_cross_rate(content,to_currency, from_currency):
    content_d = xmltodict.parse(content)
    content_d = content_d["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["ns0:getCrossRatesResponse"]["return"]["groups"]["series"]
    for item in content_d:
        if item["seriesname"]["#text"] == '1 '+to_currency+' = ? '+from_currency:
            return float(item["resultrows"]["value"]['#text'])
