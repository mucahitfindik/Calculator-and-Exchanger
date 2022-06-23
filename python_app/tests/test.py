
def test_index(app, client):
    response = client.get('/exchange', json={'amount': 120, 'toCurrency': "TRY", 'fromCurrency': "USD"})
    assert response.data == b'Hello World!'
    assert response.status_code == 200
