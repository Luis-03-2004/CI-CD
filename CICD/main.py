"""Módulo principal da aplicação FastAPI."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Retorna uma mensagem de saudação."""
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
def read_hello_name(name: str):
    """Retorna uma saudação personalizada."""
    return {"message": f"Hello, {name}"}
