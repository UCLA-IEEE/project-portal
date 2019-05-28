import app
from model.user import get_user

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

def test_user_login_failure(client):
    post = create_user(client)
    login_json = {
        'username': sample_user['username'],
        'password': sample_user['password'] + 'invalid'
    }
    rv = client.post('/auth/login', json=login_json)
    assert rv.status_code == 401

def test_user_email_verification(client):
    post = create_user(client)

    # Check that user is not verified
    get = client.get('/user/{}'.format(sample_user['username']))
    assert get.status_code == 200 and get.json['verified'] == False

    # Get the verification hash (could probably do this better but whatever lol)
    user = get_user(sample_user['username'])
    assert user.verification_code

    # Verify the user
    verify = client.post('/auth/verify/{}'.format(user.verification_code))
    assert verify.status_code == 200

    # See that user status has changed to verified
    get = client.get('/user/{}'.format(sample_user['username']))
    assert get.status_code == 200 and get.json['verified'] == True