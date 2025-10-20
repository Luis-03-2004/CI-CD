"""Módulo principal da aplicação FastAPI."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Retorna uma mensagem de saudação."""
    return {"message": "Hello World"}
