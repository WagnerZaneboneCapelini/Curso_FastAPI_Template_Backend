from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from curso_fastapi_template_backend.app import app
from curso_fastapi_template_backend.schemas import UserPublic


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@exemplo.com',
            'password': 'secreto',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@exemplo.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {
        'users': [user_schema]}


def test_update_user(client, user):
    response = client.put('/users/1', json={
        'username': 'bob',
        'email': 'bob@exemplo.com',
        'password': 'novasenha',
    },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@exemplo.com',
    }


def test_update_integrity_error(client, user):
    response = client.post('/users/', json={
        'username': 'Fausto',
        'email': 'fausto@exemplo.com',
        'password': 'segredo',
    },
    )
    response = client.put(f'/users/{user.id}', json={
        'username': 'Fausto',
        'email': 'bob@exemplo.com',
        'password': 'naoimporta',
    },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username or Email already exists'}


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_create_user_que_ja_existe(client, user):
    response = client.post('/users/', json={
        'username': user.username,
        'email': 'diferente@exemplo.com',
        'password': 'secreto',
    })

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_com_email_que_ja_existe(client, user):
    response = client.post('/users/', json={
        'username': 'joao',
        'email': user.email,
        'password': 'secreto',
    })

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Email already exists'}


def test_update_not_found_user_exercicio(client):
    response = client.put('/users/999', json={
        'username': 'ronaldo',
        'email': 'ronaldo@exemplo.com',
        'password': 'senha_ronaldo',
    })

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found'
    }


def test_delete_user_not_found_exercicio(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found'
    }


def test_get_user_especifico_exercicio(client, user):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }


def test_get_user_especifico_not_found_exercicio(client):
    response = client.get('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found'
    }
