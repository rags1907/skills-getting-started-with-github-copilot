import pytest
from fastapi.testclient import TestClient

from src import app as application


@pytest.fixture
def client():
    with TestClient(application.app) as c:
        yield c
