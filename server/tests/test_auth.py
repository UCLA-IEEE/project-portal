from tests.client import client
from tests.test_user import sample_user, create_user

def test_user_login_success(client):
    print('CLIENT: {}'.format(client))
    post = create_user(client)
    login_json = {
        'username': sample_user['username'],
        'password': sample_user['password']
    }
    rv = client.post('/auth/login', json=login_json)
    assert rv.status_code == 200

    # Ensure we got all the same attributes back
    attributes = sample_user.keys()
    for attr in attributes:
        if attr != 'password':
            assert attr in rv.json and rv.json[attr] == sample_user[attr]

    # Do not want the server to send back the password
    assert 'password' not in rv.json

def test_user_login_success(client):
    post = create_user(client)
    login_json = {
        'username': sample_user['username'],
        'password': sample_user['password'] + 'invalid'
    }
    rv = client.post('/auth/login', json=login_json)
    assert rv.status_code == 401
