import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app
from app.extensions import db
from config import TestingConfig

@pytest.fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_app(TestingConfig)
    
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(scope='function')
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


@pytest.fixture(scope='function')
def init_db(app):
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
