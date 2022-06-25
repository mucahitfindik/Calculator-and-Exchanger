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
    to_currency = "TRY"
    from_currency = "USD"
    date = dt.datetime(year=2022, month=6, day=24).date()
    cross_rate = Riksbank.exchange_currency(to_currency, from_currency, date)
    assert cross_rate == 0.0575
