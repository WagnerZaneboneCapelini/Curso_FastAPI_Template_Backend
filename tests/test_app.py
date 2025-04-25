from http import HTTPStatus

from fastapi.testclient import TestClient

from curso_fastapi_template_backend.app import app


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
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@exemplo.com',
            }
        ]
    }


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


'''
def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'User deleted'
    }
'''


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
