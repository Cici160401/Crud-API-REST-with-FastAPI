import pytest
from fastapi.testclient import TestClient
from App.main import app
from database import get_db
from App.models import Usuario
from App.utils import get_password_hash
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def crear_usuario_admin():
    db: Session = next(get_db())
    if not db.query(Usuario).filter_by(username="testadmin").first():
        user = Usuario(
            username="testadmin",
            email="admin@test.com",
            hashed_password=get_password_hash("admin123"),
            es_admin=True
        )
        db.add(user)
        db.commit()
    db.close()

@pytest.fixture(scope="session")
def admin_token(crear_usuario_admin):
    response = client.post("/auth/login", data={"username": "testadmin", "password": "admin123"})
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    return f"Bearer {access_token}"

@pytest.fixture(scope="session")
def guest_token():
    response = client.post("/auth/login/guest")
    assert response.status_code == 200
    access_token = response.json()["access_token"]
    return f"Bearer {access_token}"
