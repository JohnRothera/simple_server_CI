import pytest
from app import app


@pytest.fixture
def web_client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def test_web_address():
    return "127.0.0.1:5000"
