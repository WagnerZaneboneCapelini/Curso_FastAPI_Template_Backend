import pytest
from fastapi.testclient import TestClient

from curso_fastapi_template_backend.app import app


@pytest.fixture
def client():
    return TestClient(app)
