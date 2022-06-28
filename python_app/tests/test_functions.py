from app.functions import parse_get_cross_rate, parse_all_cross_names_response
import datetime as dt


def test_parse_all_cross_names_response():
    content = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
    <SOAP-ENV:Body>
        <ns0:getAllCrossNamesResponse xmlns:ns0="http://swea.riksbank.se/xsd">
            <return xmlns="">
                <seriesdescription xmlns="">Swedish krona</seriesdescription>
                <seriesid xmlns="">SEK</seriesid>
                <seriesname xmlns="">SEK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Austrian shilling</seriesdescription>
                <seriesid xmlns="">SEKATSPMI</seriesid>
                <seriesname xmlns="">ATS</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Australian dollar</seriesdescription>
                <seriesid xmlns="">SEKAUDPMI</seriesid>
                <seriesname xmlns="">AUD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Belgium franc</seriesdescription>
                <seriesid xmlns="">SEKBEFPMI</seriesid>
                <seriesname xmlns="">BEF</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Brazil real</seriesdescription>
                <seriesid xmlns="">SEKBRLPMI</seriesid>
                <seriesname xmlns="">BRL</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Canadian dollar</seriesdescription>
                <seriesid xmlns="">SEKCADPMI</seriesid>
                <seriesname xmlns="">CAD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Swiss francs</seriesdescription>
                <seriesid xmlns="">SEKCHFPMI</seriesid>
                <seriesname xmlns="">CHF</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Chinese yuan renminbi</seriesdescription>
                <seriesid xmlns="">SEKCNYPMI</seriesid>
                <seriesname xmlns="">CNY</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Cyprus pound</seriesdescription>
                <seriesid xmlns="">SEKCYPPMI</seriesid>
                <seriesname xmlns="">CYP</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Czech koruna</seriesdescription>
                <seriesid xmlns="">SEKCZKPMI</seriesid>
                <seriesname xmlns="">CZK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">German mark</seriesdescription>
                <seriesid xmlns="">SEKDEMPMI</seriesid>
                <seriesname xmlns="">DEM</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Danish krone</seriesdescription>
                <seriesid xmlns="">SEKDKKPMI</seriesid>
                <seriesname xmlns="">DKK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Estonian kroon</seriesdescription>
                <seriesid xmlns="">SEKEEKPMI</seriesid>
                <seriesname xmlns="">EEK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Spanish pesetas</seriesdescription>
                <seriesid xmlns="">SEKESPPMI</seriesid>
                <seriesname xmlns="">ESP</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Euroland euro</seriesdescription>
                <seriesid xmlns="">SEKEURPMI</seriesid>
                <seriesname xmlns="">EUR</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Finnish marka</seriesdescription>
                <seriesid xmlns="">SEKFIMPMI</seriesid>
                <seriesname xmlns="">FIM</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">French franc</seriesdescription>
                <seriesid xmlns="">SEKFRFPMI</seriesid>
                <seriesname xmlns="">FRF</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">pound sterling</seriesdescription>
                <seriesid xmlns="">SEKGBPPMI</seriesid>
                <seriesname xmlns="">GBP</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Greek drachmer</seriesdescription>
                <seriesid xmlns="">SEKGRDPMI</seriesid>
                <seriesname xmlns="">GRD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Hong Kong dollar</seriesdescription>
                <seriesid xmlns="">SEKHKDPMI</seriesid>
                <seriesname xmlns="">HKD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Hungarian forints</seriesdescription>
                <seriesid xmlns="">SEKHUFPMI</seriesid>
                <seriesname xmlns="">HUF</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Indonesian rupiah</seriesdescription>
                <seriesid xmlns="">SEKIDRPMI</seriesid>
                <seriesname xmlns="">IDR</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Irish pund</seriesdescription>
                <seriesid xmlns="">SEKIEPPMI</seriesid>
                <seriesname xmlns="">IEP</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Indian rupee</seriesdescription>
                <seriesid xmlns="">SEKINRPMI</seriesid>
                <seriesname xmlns="">INR</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Icelandic kronor</seriesdescription>
                <seriesid xmlns="">SEKISKPMI</seriesid>
                <seriesname xmlns="">ISK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Italian lire</seriesdescription>
                <seriesid xmlns="">SEKITLPMI</seriesid>
                <seriesname xmlns="">ITL</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Japanese yen</seriesdescription>
                <seriesid xmlns="">SEKJPYPMI</seriesid>
                <seriesname xmlns="">JPY</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">South Korean won</seriesdescription>
                <seriesid xmlns="">SEKKRWPMI</seriesid>
                <seriesname xmlns="">KRW</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Kuwaiti dinar</seriesdescription>
                <seriesid xmlns="">SEKKWDPMI</seriesid>
                <seriesname xmlns="">KWD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Lithuanian litas</seriesdescription>
                <seriesid xmlns="">SEKLTLPMI</seriesid>
                <seriesname xmlns="">LTL</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Latvian lat</seriesdescription>
                <seriesid xmlns="">SEKLVLPMI</seriesid>
                <seriesname xmlns="">LVL</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Moroccan dirham (MAD)</seriesdescription>
                <seriesid xmlns="">SEKMADPMI</seriesid>
                <seriesname xmlns="">MAD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Mexican nuevo peso</seriesdescription>
                <seriesid xmlns="">SEKMXNPMI</seriesid>
                <seriesname xmlns="">MXN</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Malaysian ringgit</seriesdescription>
                <seriesid xmlns="">SEKMYRPMI</seriesid>
                <seriesname xmlns="">MYR</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Dutch guilder</seriesdescription>
                <seriesid xmlns="">SEKNLGPMI</seriesid>
                <seriesname xmlns="">NLG</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Norwegian krone</seriesdescription>
                <seriesid xmlns="">SEKNOKPMI</seriesid>
                <seriesname xmlns="">NOK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">New Zealand dollar</seriesdescription>
                <seriesid xmlns="">SEKNZDPMI</seriesid>
                <seriesname xmlns="">NZD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Polish zloty (PLN)</seriesdescription>
                <seriesid xmlns="">SEKPLNPMI</seriesid>
                <seriesname xmlns="">PLN</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Portuguese escudo</seriesdescription>
                <seriesid xmlns="">SEKPTEPMI</seriesid>
                <seriesname xmlns="">PTE</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Russian rouble</seriesdescription>
                <seriesid xmlns="">SEKRUBPMI</seriesid>
                <seriesname xmlns="">RUB</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Saudi Arabian riyal</seriesdescription>
                <seriesid xmlns="">SEKSARPMI</seriesid>
                <seriesname xmlns="">SAR</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Singapore dollar</seriesdescription>
                <seriesid xmlns="">SEKSGDPMI</seriesid>
                <seriesname xmlns="">SGD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Slovenian tolar</seriesdescription>
                <seriesid xmlns="">SEKSITPMI</seriesid>
                <seriesname xmlns="">SIT</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Slovakian koruna</seriesdescription>
                <seriesid xmlns="">SEKSKKPMI</seriesid>
                <seriesname xmlns="">SKK</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Thai baht</seriesdescription>
                <seriesid xmlns="">SEKTHBPMI</seriesid>
                <seriesname xmlns="">THB</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Turkish lira</seriesdescription>
                <seriesid xmlns="">SEKTRLPMI</seriesid>
                <seriesname xmlns="">TRL</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">Turkish new lira</seriesdescription>
                <seriesid xmlns="">SEKTRYPMI</seriesid>
                <seriesname xmlns="">TRY</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">US dollar</seriesdescription>
                <seriesid xmlns="">SEKUSDPMI</seriesid>
                <seriesname xmlns="">USD</seriesname>
            </return>
            <return xmlns="">
                <seriesdescription xmlns="">South African rand</seriesdescription>
                <seriesid xmlns="">SEKZARPMI</seriesid>
                <seriesname xmlns="">ZAR</seriesname>
            </return>
        </ns0:getAllCrossNamesResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""
    cross_names = parse_all_cross_names_response(content)
    actual_cross_names = {
        "ATS": "Austrian shilling",
        "AUD": "Australian dollar",
        "BEF": "Belgium franc",
        "BRL": "Brazil real",
        "CAD": "Canadian dollar",
        "CHF": "Swiss francs",
        "CNY": "Chinese yuan renminbi",
        "CYP": "Cyprus pound",
        "CZK": "Czech koruna",
        "DEM": "German mark",
        "DKK": "Danish krone",
        "EEK": "Estonian kroon",
        "ESP": "Spanish pesetas",
        "EUR": "Euroland euro",
        "FIM": "Finnish marka",
        "FRF": "French franc",
        "GBP": "pound sterling",
        "GRD": "Greek drachmer",
        "HKD": "Hong Kong dollar",
        "HUF": "Hungarian forints",
        "IDR": "Indonesian rupiah",
        "IEP": "Irish pund",
        "INR": "Indian rupee",
        "ISK": "Icelandic kronor",
        "ITL": "Italian lire",
        "JPY": "Japanese yen",
        "KRW": "South Korean won",
        "KWD": "Kuwaiti dinar",
        "LTL": "Lithuanian litas",
        "LVL": "Latvian lat",
        "MAD": "Moroccan dirham (MAD)",
        "MXN": "Mexican nuevo peso",
        "MYR": "Malaysian ringgit",
        "NLG": "Dutch guilder",
        "NOK": "Norwegian krone",
        "NZD": "New Zealand dollar",
        "PLN": "Polish zloty (PLN)",
        "PTE": "Portuguese escudo",
        "RUB": "Russian rouble",
        "SAR": "Saudi Arabian riyal",
        "SEK": "Swedish krona",
        "SGD": "Singapore dollar",
        "SIT": "Slovenian tolar",
        "SKK": "Slovakian koruna",
        "THB": "Thai baht",
        "TRL": "Turkish lira",
        "TRY": "Turkish new lira",
        "USD": "US dollar",
        "ZAR": "South African rand"}
    assert cross_names == actual_cross_names


def test_parse_get_cross_rate_for_holidays():
    to_currency = "TRY"
    from_currency = "USD"
    content = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
    <SOAP-ENV:Body>
        <ns0:getCrossRatesResponse xmlns:ns0="http://swea.riksbank.se/xsd">
            <return xmlns="">
                <datefrom xmlns="">2022-06-24</datefrom>
                <dateto xmlns="">2022-06-24</dateto>
                <informationtext xmlns="">The Swedish banks daily calculate a fixing rate at 9.30 a.m. according to the formula: (bid+asked) / 2. At 10.05 a.m. Stockholm Stock Exchange sets a joint MID-PRICE by calculating the aggregate of the banks' fixing rates.&#xD;
&#xD;
Observations are published daily at 12.15 p.m.</informationtext>
            </return>
        </ns0:getCrossRatesResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""
    cross_rate = parse_get_cross_rate(content, to_currency, from_currency)
    assert cross_rate == -1


def test_parse_get_cross_rate_for_weekdays():
    to_currency = "TRY"
    from_currency = "USD"
    content = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
    <SOAP-ENV:Body>
        <ns0:getCrossRatesResponse xmlns:ns0="http://swea.riksbank.se/xsd">
            <return xmlns="">
                <datefrom xmlns="">2022-06-23</datefrom>
                <dateto xmlns="">2022-06-23</dateto>
                <informationtext xmlns="">The Swedish banks daily calculate a fixing rate at 9.30 a.m. according to the formula: (bid+asked) / 2. At 10.05 a.m. Stockholm Stock Exchange sets a joint MID-PRICE by calculating the aggregate of the banks' fixing rates.&#xD;
&#xD;
Observations are published daily at 12.15 p.m.</informationtext>
                <groups xmlns="">
                    <groupid xmlns="">130</groupid>
                    <groupname xmlns="">Currencies against Swedish kronor</groupname>
                    <series xmlns="">
                        <seriesid1 xmlns="">SEKTRYPMI</seriesid1>
                        <seriesid2 xmlns="">SEKUSDPMI</seriesid2>
                        <seriesname xmlns="">1 TRY = ? USD</seriesname>
                        <resultrows xmlns="">
                            <date xmlns="">2022-06-23</date>
                            <period xmlns:ns1="http://www.w3.org/2001/XMLSchema-instance" xmlns="" ns1:nil="true"/>
                            <average xmlns:ns1="http://www.w3.org/2001/XMLSchema-instance" xmlns="" ns1:nil="true"/>
                            <value xmlns="">5.75E-2</value>
                        </resultrows>
                    </series>
                    <series xmlns="">
                        <seriesid1 xmlns="">SEKUSDPMI</seriesid1>
                        <seriesid2 xmlns="">SEKTRYPMI</seriesid2>
                        <seriesname xmlns="">1 USD = ? TRY</seriesname>
                        <resultrows xmlns="">
                            <date xmlns="">2022-06-23</date>
                            <period xmlns:ns1="http://www.w3.org/2001/XMLSchema-instance" xmlns="" ns1:nil="true"/>
                            <average xmlns:ns1="http://www.w3.org/2001/XMLSchema-instance" xmlns="" ns1:nil="true"/>
                            <value xmlns="">1.73866E1</value>
                        </resultrows>
                    </series>
                </groups>
            </return>
        </ns0:getCrossRatesResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""
    cross_rate = parse_get_cross_rate(content, to_currency, from_currency)
    assert cross_rate == 17.3866
