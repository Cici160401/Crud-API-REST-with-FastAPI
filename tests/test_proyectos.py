from fastapi.testclient import TestClient
from App.main import app  # Asegúrate que tu archivo main.py expone `app`
from dotenv import load_dotenv
import pytest
import os

load_dotenv(".env.test")

token = os.getenv("TEST_TOKEN")

client = TestClient(app)

# 🔒 Usa un token válido (puedes mockear luego, pero por ahora puedes probar con el real)
#token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrYXJsYSIsImV4cCI6MTc1MzYxODc1NX0.in2s0JImTrTo00zFXFdqP5Ewn3dODXlRJFiTMQEwuF8"

def test_crear_proyecto_exitoso():
    response = client.post(
        "/proyectos/",  # Ajusta si tu ruta es diferente
        headers={"Authorization": token},
        json={
            "nombre": "Proyecto Test",
            "descripcion": "Descripción de prueba",
            "tecnologias": "Python, FastAPI",
            "url_repo": "https://github.com/karla/test",
            "url_demo": "https://github.com/karla/test",
            "imagen": "https://github.com/karla/test",
            "estado": "en_proceso",
            "destacado": True,
            "categorias_ids": []
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Proyecto Test"
    assert data["estado"] == "en_proceso"

def test_obtener_proyectos():
    response = client.get("/proyectos/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(p["nombre"] == "Proyecto Test" for p in data)

def test_obtener_proyecto_por_id():
    # Creamos un nuevo proyecto para obtener su ID
    response_post = client.post(
        "/proyectos/",
        headers={"Authorization": token},
        json={
            "nombre": "Proyecto Individual",
            "descripcion": "Probando GET por ID",
            "tecnologias": "Python",
            "url_repo": "https://github.com/karla/individual",
            "url_demo": None,
            "imagen": None,
            "estado": "terminado",
            "destacado": False,
            "categorias_ids": []
        }
    )
    assert response_post.status_code == 200
    data_post = response_post.json()
    proyecto_id = data_post["id"]

    # Ahora lo buscamos por ID
    response_get = client.get(f"/proyectos/{proyecto_id}")
    assert response_get.status_code == 200
    data_get = response_get.json()
    assert data_get["nombre"] == "Proyecto Individual"
    assert data_get["estado"] == "terminado"


def test_obtener_proyecto_no_existente():
    response = client.get("/proyectos/999999")  # ID que seguro no existe
    assert response.status_code == 404

def test_actualizar_proyecto():
    # Creamos un proyecto de prueba
    response_post = client.post(
        "/proyectos/",
        headers={"Authorization": token},
        json={
            "nombre": "Proyecto Actualizable",
            "descripcion": "Original",
            "tecnologias": "Python",
            "url_repo": "https://github.com/karla/original",
            "url_demo": None,
            "imagen": None,
            "estado": "en_proceso",
            "destacado": False,
            "categorias_ids": []
        }
    )
    assert response_post.status_code == 200
    proyecto = response_post.json()
    proyecto_id = proyecto["id"]

    # Ahora lo actualizamos
    response_put = client.put(
        f"/proyectos/{proyecto_id}",
        headers={"Authorization": token},
        json={
            "nombre": "Proyecto Actualizado",
            "descripcion": "Modificado",
            "estado": "terminado"
        }
    )
    assert response_put.status_code == 200
    updated = response_put.json()
    assert updated["nombre"] == "Proyecto Actualizado"
    assert updated["descripcion"] == "Modificado"
    assert updated["estado"] == "terminado"

def test_eliminar_proyecto():
    # Primero, creamos un proyecto para luego eliminarlo
    response_post = client.post(
        "/proyectos/",
        headers={"Authorization": token},
        json={
            "nombre": "Proyecto Eliminable",
            "descripcion": "Este será eliminado",
            "tecnologias": "FastAPI",
            "url_repo": "https://github.com/karla/eliminar",
            "url_demo": None,
            "imagen": None,
            "estado": "en_proceso",
            "destacado": False,
            "categorias_ids": []
        }
    )
    assert response_post.status_code == 200
    proyecto_id = response_post.json()["id"]

    # Lo eliminamos
    response_delete = client.delete(
        f"/proyectos/{proyecto_id}",
        headers={"Authorization": token}
    )
    assert response_delete.status_code == 204 

    # Verificamos que ya no existe
    response_get = client.get(f"/proyectos/{proyecto_id}")
    assert response_get.status_code == 404