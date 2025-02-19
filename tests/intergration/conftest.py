import pytest

from src.app import create_app


@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000"


@pytest.fixture
def client():
    """Fixture to create a test client using the Flask test framework."""
    app = create_app(testing=True)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
