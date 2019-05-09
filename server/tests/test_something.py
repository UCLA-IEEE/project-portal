import pytest
from app import app

@pytest.fixture
def client():
    # db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    # app.config['TESTING'] = True
    app.testing = True
    client = app.test_client()

    # with app.app_context():
    #     flaskr.init_db()

    yield client

    # os.close(db_fd)
    # os.unlink(flaskr.app.config['DATABASE'])

def test_something(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'hello'