from jinja2 import Environment, PackageLoader


class ConfigureSoap:
    env = Environment(loader=PackageLoader('app', 'templates'))
    headers = {'content-type': 'application/soap+xml'}

    @classmethod
    def soap_all_cross_names(cls):
        ConfigureSoap.headers['action'] = 'urn:getAllCrossNames'
        template = ConfigureSoap.env.get_template('soapRequests/AllCrossNames.xml')
        body = template.render()
        return body, ConfigureSoap.headers

    @classmethod
    def soap_cross_rates(cls, series_id1, series_id2, date):
        ConfigureSoap.headers['action'] = 'urn:getCrossRates'
        template = ConfigureSoap.env.get_template('soapRequests/GetCrossRates.xml')
        body = template.render()
        series_id1, series_id2 = ConfigureSoap.__set_series_ids(series_id1, series_id2)
        date_from, date_to = date, date
        return body.format(series_id1=series_id1, series_id2=series_id2, date_from=date_from,
                           date_to=date_to), ConfigureSoap.headers

    @classmethod
    def __set_series_ids(cls, series_id1, series_id2):
        if series_id1 != "SEK" and series_id2 != "SEK":
            return "SEK" + series_id1 + "PMI", "SEK" + series_id2 + "PMI"

        elif series_id1 == "SEK" and series_id2 == "SEK":
            return "SEK", "SEK"
        return "SEK" + series_id1 + "PMI" if series_id1 != "SEK" else "SEK" + series_id2 + "PMI", series_id1 \
            if series_id1 == "SEK" else series_id2
