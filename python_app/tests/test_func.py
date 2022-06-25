import requests


def test_get_currency_list(app, client):
    response = client.get('/currency-list')
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
    assert response.get_json() == actual_cross_names
    assert response.status_code == 200


def test_get_exchanged_result(app, client):
    body = {'amount': 120, 'toCurrency': "TRY", 'fromCurrency': "USD", "date": "2022-06-23"}
    response = client.get('/exchange', json=body)
    assert response.get_json()['result'] == body['amount']*0.0575