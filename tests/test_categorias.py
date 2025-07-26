from fastapi.testclient import TestClient
from App.main import app
from dotenv import load_dotenv
import os
import pytest
import uuid


load_dotenv(".env.test")

token = os.getenv("TEST_TOKEN")

client = TestClient(app)


def test_crear_categoria():
    nombre_unico = f"categoria-{uuid.uuid4().hex[:8]}"
    response = client.post(
        "/categorias/",
        headers={"Authorization": token},
        json={"nombre": nombre_unico}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == nombre_unico

def test_obtener_categorias():
    response = client.get("/categorias/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Esperamos que al menos haya alguna

def test_obtener_categoria_por_id():
    # Creamos un nuevo proyecto para obtener su ID
    response_post = client.post(
        "/categorias/",
        headers={"Authorization": token},
        json={
            "nombre": "Categoria_Prueba4"            
        }
    )
    assert response_post.status_code == 200
    data_post = response_post.json()
    categoria_id = data_post["id"]

    # Ahora lo buscamos por ID
    response_get = client.get(f"/categorias/{categoria_id}")
    assert response_get.status_code == 200
    data_get = response_get.json()
    assert data_get["nombre"] == "Categoria_Prueba4"

def test_obtener_categoria_no_existente():
    response = client.get("/categorias/999999")  # ID que seguro no existe
    assert response.status_code == 404
    
def test_actualizar_categorias():
    # Creamos un proyecto de prueba
    response_post = client.post(
        "/categorias/",
        headers={"Authorization": token},
        json={
            "nombre": "Categoria Actualizable4"            
        }
    )
    assert response_post.status_code == 200
    categoria = response_post.json()
    categoria_id = categoria["id"]

    # Ahora lo actualizamos
    response_put = client.put(
        f"/categorias/{categoria_id}",
        headers={"Authorization": token},
        json={
            "nombre": "Categoria Actualizada4"            
        }
    )
    assert response_put.status_code == 200
    updated = response_put.json()
    assert updated["nombre"] == "Categoria Actualizada4"

def test_eliminar_categoria():
    # Primero, creamos un proyecto para luego eliminarlo
    response_post = client.post(
        "/categorias/",
        headers={"Authorization": token},
        json={
            "nombre": "Categoria Eliminable"
        }
    )
    assert response_post.status_code == 200
    categoria_id = response_post.json()["id"]

    # Lo eliminamos
    response_delete = client.delete(
        f"/categorias/{categoria_id}",
        headers={"Authorization": token}
    )
    assert response_delete.status_code == 204 

    # Verificamos que ya no existe
    response_get = client.get(f"/categorias/{categoria_id}")
    assert response_get.status_code == 404
    