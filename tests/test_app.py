from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from curso_fastapi_template_backend.app import app


@pytest.mark.order(1)
def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


@pytest.mark.order(2)
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


@pytest.mark.order(3)
def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@exemplo.com',
            }
        ]
    }


@pytest.mark.order(4)
def test_update_user(client):
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


@pytest.mark.order(5)
def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted'
    }


@pytest.mark.order(6)
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


@pytest.mark.order(7)
def test_delete_user_not_found_exercicio(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found'
    }


@pytest.mark.order(8)
def test_get_user_especifico_exercicio(client):
    # Criando o usuário antes de deletá-lo
    client.post('/users/', json={
        'username': 'bob',
        'email': 'bob@exemplo.com',
        'password': 'secreto'})

    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'bob',
        'email': 'bob@exemplo.com',
    }


@pytest.mark.order(9)
def test_get_user_especifico_not_found_exercicio(client):
    response = client.get('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found'
    }
