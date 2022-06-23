import xmltodict


def parse_all_corse_names_response(content):
    content_d = xmltodict.parse(content)
    content_d = content_d["SOAP-ENV:Envelope"]["SOAP-ENV:Body"]["ns0:getAllCrossNamesResponse"]["return"]
    corse_names = {}
    for item in content_d:
        corse_names[item["seriesname"]["#text"]] = item["seriesdescription"]["#text"]
    return corse_names
