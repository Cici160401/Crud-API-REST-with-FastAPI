Portafolio Projects API

Una API REST construida con FastAPI para administrar proyectos, categorías y comentarios en un portafolio de desarrollador. Ideal para integrarse con un frontend o servir como backend autónomo.

🚀 Tecnologías usadas

FastAPI

SQLAlchemy + MySQL (via ORM)

Pydantic (validación de datos)

JWT Auth (OAuth Bearer) (autenticación con tokens)

pytest (para pruebas automatizadas)

Render (para despliegue)

🔎 Características principales

💼 Proyectos

Crear, listar, obtener por ID, actualizar y eliminar proyectos

Asociar proyectos a una o más categorías

Atributos:

nombre, descripcion, tecnologias, estado, imagen, url_repo, url_demo, destacado, fecha_creacion

📅 Categorías

Crear, listar, obtener por ID, actualizar y eliminar categorías

Las categorías se pueden asociar a proyectos

💬 Comentarios

Crear comentarios por usuarios invitados o autenticados

Listar todos los comentarios o filtrar por proyecto_id

Eliminar comentarios (solo admin)

🔐 Autenticación y roles

Autenticación con JWT:

/login: para admin

/login/guest: para obtener un token como invitado

Roles disponibles:

admin: puede crear, editar y eliminar todo

guest: solo puede crear comentarios y ver proyectos/categorías

✅ Endpoints principales (resumen)

Proyectos

GET     /proyectos/            # Listar proyectos
POST    /proyectos/            # Crear nuevo proyecto (admin)
GET     /proyectos/{id}        # Ver un proyecto específico
PUT     /proyectos/{id}        # Actualizar proyecto (admin)
DELETE  /proyectos/{id}        # Eliminar proyecto (admin)

Categorías

GET     /categorias/           # Listar categorías
POST    /categorias/           # Crear categoría (admin)
GET     /categorias/{id}       # Ver categoría por ID
PUT     /categorias/{id}       # Actualizar categoría (admin)
DELETE  /categorias/{id}       # Eliminar categoría (admin)

Comentarios

GET     /comentarios/                          # Listar todos los comentarios
GET     /comentarios/proyectos/{id}            # Comentarios de un proyecto
POST    /comentarios/                          # Crear comentario (cualquiera)
DELETE  /comentarios/{id}                      # Eliminar comentario (admin)

⚙️ Instalación local (opcional)

git clone https://github.com/tuusuario/portafolio-api.git
cd portafolio-api
python -m venv env
source env/bin/activate  # o env\Scripts\activate en Windows
pip install -r requirements.txt
uvicorn App.main:app --reload

Visita: http://localhost:8000/docs

💡 Notas adicionales

Las pruebas están en tests/

Puedes correrlas con: pytest tests/test_...

Archivo .env define variables sensibles como la DB y secret key

Despliegue recomendado en Render

🙏 Agradecimientos

Gracias a FastAPI y a todos los que me brindaron motivación ✨