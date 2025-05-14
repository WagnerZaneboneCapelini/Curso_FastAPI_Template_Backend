from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from curso_fastapi_template_backend.app import app
from curso_fastapi_template_backend.schemas import UserPublic
from curso_fastapi_template_backend.security import SECRET_KEY, create_access_token


def test_jwt_invalid_email(client):
    data = {'no-email': 'test'}
    token = create_access_token(data)
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_jwt_email_ok_user_not_exist(client):
    data = {'sub': 'test@test'}
    token = create_access_token(data)
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
