

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
    assert response.get_json()["currency_list"] == actual_cross_names
    assert response.status_code == 200


def test_post_exchanged_result_without_body(app, client):
    response = client.post('/exchange').get_json()
    assert response == {"error": 'The body of this request is unexpected.'}


def test_post_exchanged_result_with_empty_body(app, client):
    body = {}
    response = client.post('/exchange', json=body).get_json()
    assert response == {"error": "No amount provided!"}


def test_post_exchanged_result_with_unsupported_currency(app, client):
    body = {'amount': 120, 'toCurrency': ["USZ"], 'fromCurrency': "TRY", "date": "2022-06-23"}
    response = client.post('/exchange', json=body).get_json()
    assert response == {"error": "Currency list doesn't include USZ."}


def test_post_exchanged_result(app, client):
    body = {'amount': 120, 'toCurrency': ["USD"], 'fromCurrency': "TRY", "date": "2022-06-23"}
    response = client.post('/exchange', json=body).get_json()
    assert response == [{
        "cross_rate": 0.0575,
        "result": 6.9,
        "to_currency": "USD"
    }]


def test_post_exchanged_result_with_multi_to_currency(app, client):
    body = {'amount': 120, 'toCurrency': ["DKK", "USD"], 'fromCurrency': "TRY", "date": "2022-06-23"}
    response = client.post('/exchange', json=body).get_json()
    assert response == [{
        "cross_rate": 0.4068,
        "result": 48.816,
        "to_currency": "DKK"
    }, {
        "cross_rate": 0.0575,
        "result": 6.9,
        "to_currency": "USD"
    }]
