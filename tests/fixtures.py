import pytest

from rmon.app import create_ap
from rmon.models import Server
from rmon.models import db as database

@pytest.fixture
def app():
    return create_app()

@pytest.yield_fixture
def db(app):
    with app.app_context():
        database.create_all()
        yield database
        database.drop_all()

def server(db):
    server = Server(name='redis_test', description='this is a test record',
            host='127.0.0.1', port='6379')
    server.save()
    return server

