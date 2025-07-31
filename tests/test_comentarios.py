from fastapi.testclient import TestClient
from App.main import app
import pytest

client = TestClient(app)

def crear_proyecto_temporal(token):
    response = client.post(
        "/proyectos/",
        headers={"Authorization": token},
        json={
            "nombre": "Proyecto Test Comentario",
            "descripcion": "Proyecto para probar comentarios",
            "tecnologias": "Python, FastAPI",
            "url_repo": "http://test.com/repo",
            "url_demo": "http://test.com/demo",
            "imagen": "http://test.com/imagen.png",
            "estado": "en_proceso",
            "destacado": False,
            "categorias_ids": [1]
        }
    )
    print("🚨 Proyecto response:", response.status_code, response.json())
    assert response.status_code == 200
    return response.json()["id"]


@pytest.mark.usefixtures("guest_token")
def test_crear_comentario(admin_token, guest_token):
    proyecto_id = crear_proyecto_temporal(admin_token)

    response = client.post(
        "/comentarios/",
        headers={"Authorization": guest_token},
        json={
            "autor": "guest",
            "contenido": "Este es un comentario generado por una prueba",
            "proyecto_id": proyecto_id
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["autor"] == "guest"
    assert data["contenido"] == "Este es un comentario generado por una prueba"
    assert data["proyecto_id"] == proyecto_id

def test_listar_todos_los_comentarios():
    response = client.get("/comentarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#@pytest.mark.usefixtures("guest_token")
def test_obtener_comentarios_por_proyecto(guest_token, admin_token):
    proyecto_id = crear_proyecto_temporal(admin_token)

    # Crear un comentario primero
    client.post(
        "/comentarios/",
        headers={"Authorization": guest_token},
        json={
            "autor": "IGNORADO_POR_BACKEND",
            "contenido": "Este es un comentario generado por una prueba",
            "proyecto_id": proyecto_id
        }
    )

    response = client.get(f"/comentarios/proyectos/{proyecto_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(com["autor"] == "guest" for com in data)

#@pytest.mark.usefixtures("guest_token")
def test_eliminar_comentario(admin_token, guest_token):
    proyecto_id = crear_proyecto_temporal(admin_token)

    # Crear comentario
    response_post = client.post(
        "/comentarios/",
        headers={"Authorization": guest_token},
        json={
            "autor": "IGNORADO_POR_BACKEND",
            "contenido": "Comentario a eliminar",
            "proyecto_id": proyecto_id
        }
    )
    assert response_post.status_code == 200
    comentario_id = response_post.json()["id"]

    # Eliminar como admin
    response_delete = client.delete(
        f"/comentarios/{comentario_id}",
        headers={"Authorization": admin_token}
    )
    assert response_delete.status_code == 204