
from fastapi.testclient import TestClient
from App.main import app
import pytest

client = TestClient(app)

def test_crear_proyecto_exitoso(admin_token):
    response = client.post(
        "/proyectos/",
        headers={"Authorization": admin_token},
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

def test_obtener_proyecto_por_id(admin_token):
    response_post = client.post(
        "/proyectos/",
        headers={"Authorization": admin_token},
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
    proyecto_id = response_post.json()["id"]

    response_get = client.get(f"/proyectos/{proyecto_id}")
    assert response_get.status_code == 200
    assert response_get.json()["nombre"] == "Proyecto Individual"

def test_obtener_proyecto_no_existente():
    response = client.get("/proyectos/999999")
    assert response.status_code == 404

def test_actualizar_proyecto(admin_token):
    response_post = client.post(
        "/proyectos/",
        headers={"Authorization": admin_token},
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
    proyecto_id = response_post.json()["id"]

    response_put = client.put(
        f"/proyectos/{proyecto_id}",
        headers={"Authorization": admin_token},
        json={
            "nombre": "Proyecto Actualizado",
            "descripcion": "Modificado",
            "estado": "terminado"
        }
    )
    assert response_put.status_code == 200
    assert response_put.json()["nombre"] == "Proyecto Actualizado"

def test_eliminar_proyecto(admin_token):
    response_post = client.post(
        "/proyectos/",
        headers={"Authorization": admin_token},
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

    response_delete = client.delete(f"/proyectos/{proyecto_id}", headers={"Authorization": admin_token})
    assert response_delete.status_code == 204

    response_get = client.get(f"/proyectos/{proyecto_id}")
    assert response_get.status_code == 404
