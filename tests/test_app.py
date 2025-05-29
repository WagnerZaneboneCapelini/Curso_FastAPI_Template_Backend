from http import HTTPStatus
import pytest


from fastapi.testclient import TestClient
from curso_fastapi_template_backend.app import app


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
