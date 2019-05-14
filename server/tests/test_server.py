from tests.client import client

def test_something(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data
