
from fastapi.testclient import TestClient
from App.main import app
import pytest

client = TestClient(app)

def eliminar_categoria_si_existe(nombre: str, admin_token: str):
    response = client.get("/categorias/")
    for cat in response.json():
        if cat["nombre"] == nombre:
            client.delete(f"/categorias/{cat['id']}", headers={"Authorization": admin_token})

def test_crear_categoria_exitoso(admin_token):
    eliminar_categoria_si_existe("Categoria Test", admin_token)

    response = client.post(
        "/categorias/",
        headers={"Authorization": admin_token},
        json={"nombre": "Categoria Test"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Categoria Test"
    

def test_obtener_categorias():
    response = client.get("/categorias/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_obtener_categoria_por_id(admin_token):
    eliminar_categoria_si_existe("Categoria Individual", admin_token)

    response_post = client.post(
        "/categorias/",
        headers={"Authorization": admin_token},
        json={"nombre": "Categoria Individual"}
    )
    assert response_post.status_code == 200
    categoria_id = response_post.json()["id"]

    response_get = client.get(f"/categorias/{categoria_id}")
    assert response_get.status_code == 200
    assert response_get.json()["nombre"] == "Categoria Individual"

def test_obtener_categoria_no_existente():
    response = client.get("/categorias/999999")
    assert response.status_code == 404

def test_actualizar_categorias(admin_token):
    eliminar_categoria_si_existe("Categoria Actualizable", admin_token)
    eliminar_categoria_si_existe("Categoria Actualizada", admin_token)

    response_post = client.post(
        "/categorias/",
        headers={"Authorization": admin_token},
        json={"nombre": "Categoria Actualizable"}
    )
    assert response_post.status_code == 200
    categoria_id = response_post.json()["id"]

    response_put = client.put(
        f"/categorias/{categoria_id}",
        headers={"Authorization": admin_token},
        json={"nombre": "Categoria Actualizada"}
    )
    assert response_put.status_code == 200
    assert response_put.json()["nombre"] == "Categoria Actualizada"

def test_eliminar_categoria(admin_token):
    # Elimina si ya existe una categoría con ese nombre
    response_list = client.get("/categorias/")
    for cat in response_list.json():
        if cat["nombre"] == "Categoria Eliminable":
            client.delete(f"/categorias/{cat['id']}", headers={"Authorization": admin_token})

    # Crear categoría nueva
    response_post = client.post(
        "/categorias/",
        headers={"Authorization": admin_token},
        json={"nombre": "Categoria Eliminable"}
    )
    assert response_post.status_code == 200
    categoria_id = response_post.json()["id"]

    # Eliminarla
    response_delete = client.delete(
        f"/categorias/{categoria_id}",
        headers={"Authorization": admin_token}
    )
    assert response_delete.status_code == 200
    data = response_delete.json()
    assert data["mensaje"] == "Categoría eliminada con éxito"

    # Verifica que ya no existe
    response_get = client.get(f"/categorias/{categoria_id}")
    assert response_get.status_code == 404