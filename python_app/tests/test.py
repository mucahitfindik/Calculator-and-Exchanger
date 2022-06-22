
def test_index(app, client):
    response = client.get('/exchange')
    assert response.data == b'Hello World!'
    assert response.status_code == 200
