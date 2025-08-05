# CRUD API REST con FastAPI

<p align="center">
  <a href="https://github.com/Cici160401/Crud-API-REST-with-FastAPI/actions/workflows/test.yml">
    <img src="https://github.com/Cici160401/Crud-API-REST-with-FastAPI/actions/workflows/test.yml/badge.svg" alt="Test">
  </a>
  <img src="https://img.shields.io/github/last-commit/Cici160401/Crud-API-REST-with-FastAPI" alt="Último commit">
  <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python 3.12">
  <a href="https://render.com/images/deploy-to-render-button.svg">
    <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
  </a>
  <img src="https://img.shields.io/badge/Hosted_on-Render-4287f5?logo=render&logoColor=white&style=flat-square" alt="Hosted on Render">
</p>

🔗 **URL en producción:** [https://crud-api-rest-with-fastapi.onrender.com](https://crud-api-rest-with-fastapi.onrender.com)

---

## 📋 Tabla de contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)  
2. [Funcionalidades](#funcionalidades)  
3. [Tecnologías utilizadas](#tecnologías-utilizadas)  
4. [Testing con GitHub Actions](#testing-con-github-actions)  
5. [Instalación y uso local](#instalación-y-uso-local)  
6. [Endpoints principales](#endpoints-principales)  
7. [Estructura del proyecto](#estructura-del-proyecto)  
8. [Licencia](#licencia)  
9. [Autor](#autor)  

---

## 📌 Descripción del Proyecto

Este proyecto es una **API REST** desarrollada con **FastAPI** para gestionar un portafolio de proyectos. Entre sus características principales:

- Autenticación JWT.
- Modelos relacionados mediante SQLAlchemy.
- Roles de usuario: **admin** e **invitado**.
- Pruebas automatizadas con **pytest**.
- Preparada para integrarse con un frontend y desplegarse en producción.

---

## 🚀 Funcionalidades

- **Registro y login** de usuario con JWT.  
- CRUD completo de **proyectos**.  
- Gestión de **categorías** de proyectos.  
- **Comentarios** asociados a proyectos (incluye invitados autenticados).  
- **Protección de rutas** según rol.  
- **Validaciones** con Pydantic.  

---

## 🛠 Tecnologías utilizadas

- **FastAPI**  
- **SQLAlchemy**  
- **MySQL**  
- **Pydantic**  
- **Passlib** (hashing de contraseñas)  
- **PyJWT**  
- **pytest**  
- **GitHub Actions** (CI)  

---

## 🧪 Testing con GitHub Actions

El flujo de trabajo en `.github/workflows/test.yml`:

1. Se ejecuta en cada **push**.  
2. Instala dependencias.  
3. Corre los tests automáticos (`pytest tests/test_...`).  

Además, en la carpeta `.vscode` encontrarás `tasks.json` para ejecutar tests con el botón **Run all** (Ctrl + Shift + P → Run ALL tests).  

---

## 🔧 Instalación y uso local

### En Linux/Mac

source venv/bin/activate

## Windows
venv\Scripts\activate

## Instala las dependencias:
pip install -r requirements.txt

## Inicia el servidor:
uvicorn App.main:app --reload
Abre la documentación interactiva en:
http://localhost:8000/docs

----
### 📆 Endpoints principales
```plaintext
Método	Ruta	Descripción	Acceso
POST	/login	Login de usuario	Público
POST	/login/guest	Login como invitado (token sin BD)	Público
GET	/proyectos/	Listar todos los proyectos	Público
POST	/proyectos/	Crear proyecto	Solo admin
GET	/categorias/	Listar categorías	Público
POST	/comentarios/	Crear comentario	Usuarios autenticados
…	Consulta /docs	Lista completa generada con Swagger	—

---

### 🗄️ Estructura del proyecto

```plaintext
Crud-API-REST-with-FastAPI/
├── App/
│   ├── main.py                # Punto de entrada
│   ├── models/                # Modelos SQLAlchemy
│   ├── schemas/               # Esquemas Pydantic
│   ├── routes/                # Endpoints por entidad
│   ├── crud/                  # Lógica CRUD
│   └── auth/                  # JWT y roles
│
├── tests/                     # Pruebas con pytest
│
├── .github/
│   └── workflows/
│       └── test.yml           # CI con GitHub Actions
│
├── requirements.txt           # Dependencias
└── README.md                  # Documentación

---

📄 Licencia
Este proyecto está bajo la licencia MIT.

👤 Autor
Desarrollado con ❤️ por Cici160401
