from tests.client import client

sample_user = {
    "username": 'kathy',
    "email": 'kdaniels@gmail.com',
    "name": 'Kathy Daniels',
    "role": 'admin',
    "password": 'password'
}

def create_user(client):
    rv = client.post('/user/', json=sample_user)
    
    return rv

def test_user_basic_post_get_delete(client):
    # Create a sample user
    post = create_user(client)
    assert post.status_code == 200

    # Make sure we got an id
    data = post.json
    assert 'id' in data
    assert 'username' in data

    # Look at all users
    rv = client.get('/user/')
    print('All users: {}'.format(rv.json))
    assert rv.status_code == 200
    assert type(rv.json) == list
    assert len(rv.json) == 1

    # Get back the same user we just created
    username = data['username']
    rv = client.get('/user/{}'.format(username))
    print(rv.json)
    assert rv.status_code == 200

    # Ensure we got all the same attributes back
    attributes = sample_user.keys()
    for attr in attributes:
        if attr != 'password':
            assert attr in rv.json and rv.json[attr] == sample_user[attr]

    # Do not want the server to send back the password
    assert 'password' not in rv.json

    # Delete the user
    rv = client.delete('/user/{}'.format(username))
    assert rv.status_code == 200

    # Try to get back the deleted user for a 404
    rv = client.get('/user/{}'.format(username))
    print(rv.json)
    assert rv.status_code == 404

    # Ensure that no users left at all
    rv = client.get('/user/')
    assert rv.status_code == 200
    assert len(rv.json) == 0

def test_user_empty_post_400(client):
    # No json, should give us an error
    rv = client.post('/user/')
    assert rv.status_code == 400

def test_user_bad_post_400(client):
    rv = client.post('/user/', json={'field': 'random'})
    assert rv.status_code == 400