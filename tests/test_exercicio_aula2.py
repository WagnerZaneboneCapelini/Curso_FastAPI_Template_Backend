from http import HTTPStatus
from fastapi.testclient import TestClient
from curso_fastapi.exercicio_aula2 import app
from fastapi.responses import HTMLResponse


def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/exercicio')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
