from app.riksbank.riksbank import Riksbank
import datetime as dt


def test_get_currency_list():
    cross_names = Riksbank.get_currency_list()
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


def test_exchange_currency():
    to_currency = ["DKK"]
    from_currency = "TRY"
    amount = 120
    date = dt.datetime(year=2022, month=6, day=24).date()
    res = Riksbank.exchange_currency(amount, to_currency, from_currency, date).get_json()
    assert res == [{
        "cross_rate": 0.4068,
        "result": 48.816,
        "to_currency": "DKK"
    }]


def test_exchange_currency_with_multi_to_currency():
    to_currency = ["DKK", "USD"]
    from_currency = "TRY"
    amount = 120
    date = dt.datetime(year=2022, month=6, day=24).date()
    res = Riksbank.exchange_currency(amount, to_currency, from_currency, date).get_json()
    assert res == [{
        "cross_rate": 0.4068,
        "result": 48.816,
        "to_currency": "DKK"
    }, {
        "cross_rate": 0.0575,
        "result": 6.9,
        "to_currency": "USD"
    }]
