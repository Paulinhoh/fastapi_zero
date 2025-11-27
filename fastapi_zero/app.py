from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Minha API Bala!')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/quiz2', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <body>
            <p>Olá Mundo</p>
        </body>
    </html>
    """
