from app.riksbank.soap.configure_soap import ConfigureSoap
import datetime as dt


def test_soap_for_all_cross_names():
    body, header = ConfigureSoap.soap_all_cross_names()
    expected_header = {'content-type': 'application/soap+xml', 'action': 'urn:getAllCrossNames'}
    expected_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsd="http://swea.riksbank.se/xsd">
	<soap:Header/>

	<soap:Body>
		<xsd:getAllCrossNames>
			<languageid>en</languageid>
		</xsd:getAllCrossNames>
	</soap:Body>
</soap:Envelope>"""
    assert body == expected_body
    assert header == expected_header


def test_soap_for_get_cross_rates_with_sek_sek():
    to_currency = "SEK"
    from_currency = "SEK"
    date = dt.datetime(year=2022, month=6, day=23).date()
    body, header = ConfigureSoap.soap_cross_rates(to_currency, from_currency, date)
    expected_header = {'content-type': 'application/soap+xml', 'action': 'urn:getCrossRates'}
    expected_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsd="http://swea.riksbank.se/xsd">
	<soap:Header/>
	<soap:Body>
		<xsd:getCrossRates>
			<crossRequestParameters>
				<aggregateMethod>D</aggregateMethod>
				<!--1 or more repetitions:-->
				<crossPair>
					<seriesid1>SEK</seriesid1>
					<seriesid2>SEK</seriesid2>
				</crossPair>
				<datefrom>2022-06-23</datefrom>
				<dateto>2022-06-23</dateto>
				<languageid>en</languageid>
			</crossRequestParameters>
		</xsd:getCrossRates>
	</soap:Body>
</soap:Envelope>"""
    assert body == expected_body
    assert header == expected_header


def test_soap_for_get_cross_rates_with_sek_usd():
    to_currency = "SEK"
    from_currency = "USD"
    date = dt.datetime(year=2022, month=6, day=23).date()
    body, header = ConfigureSoap.soap_cross_rates(to_currency, from_currency, date)
    expected_header = {'content-type': 'application/soap+xml', 'action': 'urn:getCrossRates'}
    expected_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsd="http://swea.riksbank.se/xsd">
	<soap:Header/>
	<soap:Body>
		<xsd:getCrossRates>
			<crossRequestParameters>
				<aggregateMethod>D</aggregateMethod>
				<!--1 or more repetitions:-->
				<crossPair>
					<seriesid1>SEKUSDPMI</seriesid1>
					<seriesid2>SEK</seriesid2>
				</crossPair>
				<datefrom>2022-06-23</datefrom>
				<dateto>2022-06-23</dateto>
				<languageid>en</languageid>
			</crossRequestParameters>
		</xsd:getCrossRates>
	</soap:Body>
</soap:Envelope>"""
    assert body == expected_body
    assert header == expected_header


def test_soap_for_get_cross_rates_with_try_usd():
    to_currency = "TRY"
    from_currency = "USD"
    date = dt.datetime(year=2022, month=6, day=23).date()
    body, header = ConfigureSoap.soap_cross_rates(to_currency, from_currency, date)
    expected_header = {'content-type': 'application/soap+xml', 'action': 'urn:getCrossRates'}
    expected_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsd="http://swea.riksbank.se/xsd">
	<soap:Header/>
	<soap:Body>
		<xsd:getCrossRates>
			<crossRequestParameters>
				<aggregateMethod>D</aggregateMethod>
				<!--1 or more repetitions:-->
				<crossPair>
					<seriesid1>SEKTRYPMI</seriesid1>
					<seriesid2>SEKUSDPMI</seriesid2>
				</crossPair>
				<datefrom>2022-06-23</datefrom>
				<dateto>2022-06-23</dateto>
				<languageid>en</languageid>
			</crossRequestParameters>
		</xsd:getCrossRates>
	</soap:Body>
</soap:Envelope>"""
    assert body == expected_body
    assert header == expected_header
