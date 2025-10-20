"""Módulo de testes para a aplicação FastAPI."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Testa o endpoint raiz da aplicação."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_read_hello_name():
    """Testa o endpoint de saudação personalizada."""
    name_to_test = "John"
    response = client.get(f"/hello/{name_to_test}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {name_to_test}"}
