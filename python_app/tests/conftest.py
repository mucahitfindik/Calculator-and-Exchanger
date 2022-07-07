import pytest

from app.app import create_app
from app.config import TestConfig


@pytest.fixture
def app():
    flask_app = create_app(TestConfig)
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
