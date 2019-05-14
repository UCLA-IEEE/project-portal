import pytest
from app import app, db
from load_mock_data import load

@pytest.fixture
def client():
    app.config['DATABASE'] = 'sqlite:////tmp/testing.db'
    app.testing = True
    client = app.test_client()

    db.drop_all()
    db.create_all()

    yield client