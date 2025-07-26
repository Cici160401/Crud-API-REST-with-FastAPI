from fastapi.testclient import TestClient
from App.main import app
from dotenv import load_dotenv
import os
import pytest

client = TestClient(app)
load_dotenv(".env.test")

token = os.getenv("TEST_TOKEN")


def test_crear_comentario():
    proyecto_id_existente = 88  # Asegúrate que este proyecto exista

    response = client.post(
        "/comentarios/",
        json={
            "autor": "TestUser",
            "contenido": "Este es un comentario generado por una prueba2",
            "proyecto_id": proyecto_id_existente
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["autor"] == "TestUser"
    assert data["contenido"] == "Este es un comentario generado por una prueba2"
    assert data["proyecto_id"] == proyecto_id_existente

def test_listar_todos_los_comentarios():
    response = client.get("/comentarios/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obtener_comentarios_por_proyecto():
    proyecto_id = 88  # Usa el mismo proyecto del test anterior

    response = client.get(f"/comentarios/proyectos/{proyecto_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(com["autor"] == "TestUser" for com in data)

def test_eliminar_comentario():
    # Crear primero un comentario para luego eliminarlo
    proyecto_id = 88  # Asegúrate que existe este proyecto

    response_post = client.post(
        "/comentarios/",
        json={
            "autor": "EliminarTest",
            "contenido": "Este comentario será eliminado",
            "proyecto_id": proyecto_id
        }
    )
    assert response_post.status_code == 200
    comentario_id = response_post.json()["id"]

    # Ahora eliminarlo
    response_delete = client.delete(f"/comentarios/{comentario_id}", headers={"Authorization": token})
    assert response_delete.status_code == 204
    #assert response_delete.json()["mensaje"] == "Comentario eliminado con éxito"
