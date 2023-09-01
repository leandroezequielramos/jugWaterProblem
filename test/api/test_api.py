from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app, VERSION

client = TestClient(app)


def test_version():
    """checks api version."""
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == VERSION
