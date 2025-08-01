## CRUD API REST with FastAPI

![Test](https://github.com/Cici160401/Crud-API-REST-with-FastAPI/actions/workflows/test.yml/badge.svg)

![last commit](https://img.shields.io/github/last-commit/Cici160401/Crud-API-REST-with-FastAPI)

![Python](https://img.shields.io/badge/Python-3.12-blue)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Cici160401/Crud-API-REST-with-FastAPI)

![Hosted on Render](https://img.shields.io/badge/Hosted_on-Render-4287f5?logo=render&logoColor=white&style=flat-square)

Este es un proyecto de una API REST desarrollada con FastAPI, que permite gestionar un portafolio de proyectos. Incluye autenticación JWT, relaciones entre modelos, roles de usuario (admin e invitado), y pruebas automatizadas.

## 📌 Descripción del Proyecto

Esta API permite gestionar:

Usuarios con roles diferenciados (admin e invitado).

Categorías de proyectos.

Proyectos con atributos como nombre, descripción, tecnologías, links y categorización.

Comentarios asociados a proyectos.

La API está diseñada para integrarse eventualmente con un frontend y estar lista para despliegue en producción.

## 🚀 Funcionalidades

Registro y login de usuario con JWT

Creación, lectura, actualización y eliminación (CRUD) de proyectos

Asociación de proyectos a múltiples categorías

Comentarios de usuarios (incluyendo invitados autenticados)

Rutas protegidas según rol

Validaciones con Pydantic

## 🛠 Tecnologías utilizadas

FastAPI

SQLAlchemy

MySQL

Pydantic

Passlib (hashing de contraseñas)

PyJWT

pytest

GitHub Actions para CI

## 🧪 Testing con GitHub Actions

El proyecto incluye un flujo de trabajo en .github/workflows/test.yml que:

Se ejecuta en cada push

Instala dependencias

Corre los tests automáticos con pytest tests/test_....
También existe un apartado la carpeta vscode donde el archivo tasks.json te ayuda a automatizar la ejecución de los tests
dentro de VS Code con el botón Run all (Accedes con Ctrl + Shift + P y buscas Run ALL tests)

Esto asegura que cada cambio no rompa funcionalidades existentes.

## 🔧 Instalación y uso local

Clona el repositorio:

git clone https://github.com/Cici160401/Crud-API-REST-with-FastAPI.git
cd Crud-API-REST-with-FastAPI

Crea un entorno virtual e instálalo:

python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt

Inicia el servidor:

uvicorn App.main:app --reload

Abre la documentación interactiva:

http://localhost:8000/docs

## 📆 Endpoints principales

POST /login: login de usuario

POST /login/guest: login como invitado (genera token sin base de datos)

GET /proyectos/: listar todos los proyectos

POST /proyectos/: crear proyecto (solo admin)

GET /categorias/: listar categorías

POST /comentarios/: crear comentario (cualquier usuario autenticado)

Y muchos otros. Consulta /docs para ver la lista completa generada con Swagger.

## 🗄️ Estructura del proyecto

Crud-API-REST-with-FastAPI/
│
├── App/
│   ├── main.py               # Punto de entrada de la API
│   ├── models/               # Modelos de SQLAlchemy
│   ├── schemas/              # Esquemas de Pydantic
│   ├── routes/               # Endpoints agrupados por entidad
│   ├── crud/                 # Lógica CRUD
│   └── auth/                 # Lógica de autenticación (JWT, roles, etc.)
│
├── tests/                    # Pruebas automatizadas con Pytest
│
├── .github/
│   └── workflows/
│       └── test.yml          # Workflow para correr tests en GitHub Actions
│
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación principal


## Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.


Desarrollado con ❤️ por Cici160401
