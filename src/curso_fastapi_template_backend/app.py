from http import HTTPStatus

from fastapi import FastAPI

from curso_fastapi_template_backend.schemas import Message
from curso_fastapi_template_backend.routers import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
