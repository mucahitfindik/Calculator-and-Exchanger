import unittest
import datetime as dt
from app.validator.exchange.post_request import InvalidRequestParameter, InvalidCurrency, check_required_parameters, \
    check_currency_supported


class TestValidatorPostRequest(unittest.TestCase):
    currency_list = {
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

    def test_amount_not_exist(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'toCurrency': ['SEK', 'DKK'], 'fromCurrency': 'USD', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("No amount provided!" in message.exception.message)

    def test_amount_string(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': '2', 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': 'USD', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("Amount should be number!" in message.exception.message)

    def test_to_currency_not_exist(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 25, 'fromCurrency': 'USD', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("Please select the currency(s) in which you want to exchange the amount." in message.exception.message)

    def test_to_currency_empty_string(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 25, 'toCurrency': '', 'fromCurrency': 'USD', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("Please select the currency(s) in which you want to exchange the amount." in message.exception.message)

    def test_to_currency_empty_array(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 25, 'toCurrency': [], 'fromCurrency': 'USD', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("Please select the currency(s) in which you want to exchange the amount." in message.exception.message)

    def test_to_currency_number(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 25, 'toCurrency': 2, 'fromCurrency': 'USD', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("toCurrency should be array or string!" in message.exception.message)

    def test_from_currency_not_exist(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("Please select a currency of the amount." in message.exception.message)

    def test_from_currency_empty_string(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': '', 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("Please select a currency of the amount." in message.exception.message)

    def test_from_currency_array(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': ['USD'], 'date': '2022-06-27'}
            check_required_parameters(data)
        self.assertTrue("fromCurrency should be string!" in message.exception.message)

    def test_date_not_exist(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': 'USD'}
            check_required_parameters(data)
        self.assertTrue("No date provided!" in message.exception.message)

    def test_date_empty_string(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': 'USD', 'date': ''}
            check_required_parameters(data)
        self.assertTrue("No date provided!" in message.exception.message)

    def test_date_datetime_object(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': 'USD',
                    'date': dt.date.fromisoformat("2022-06-27")}
            check_required_parameters(data)
        self.assertTrue("date should be string!" in message.exception.message)

    def test_date_wrong_format(self):
        with self.assertRaises(InvalidRequestParameter) as message:
            data = {'amount': 2, 'toCurrency': ['SEK', 'DKK'], 'fromCurrency': 'USD', 'date': '2022/06/27'}
            check_required_parameters(data)
        self.assertTrue("Incorrect date format, should be YYYY-MM-DD" in message.exception.message)

    def test_from_currency_not_supported(self):
        with self.assertRaises(InvalidCurrency) as message:
            from_currency = "USZ"
            to_currency = ['SEK', 'DKK']
            check_currency_supported(from_currency, to_currency, self.currency_list)
        self.assertTrue("Currency list doesn't include " + from_currency + "." in message.exception.message)

    def test_to_currency_not_supported(self):
        with self.assertRaises(InvalidCurrency) as message:
            from_currency = "USD"
            to_currency = ['SEZ']
            check_currency_supported(from_currency, to_currency, self.currency_list)
        self.assertTrue("Currency list doesn't include " + to_currency[0] + "." in message.exception.message)
