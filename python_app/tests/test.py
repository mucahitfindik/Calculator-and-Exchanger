from flask import jsonify


def test_index(app, client):
    response = client.get('/exchange', json={'amount': 120, 'toCurrency': "TRY", 'fromCurrency': "USD"})
    assert response.get_json()["result"] == 'Hello World!'
    assert response.status_code == 200
