import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client

def test_home_page_status(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_page_content(client):
    response = client.get("/")
    assert b"Flask CI/CD Demo using Jenkins" in response.data

def test_hello_endpoint(client):
    response = client.post("/hello", data={"username": "Jenkins"})
    assert response.status_code == 200
    assert b"Hello Jenkins" in response.data
