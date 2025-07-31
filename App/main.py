from fastapi import FastAPI
from App.routes import proyecto, categorias, comentarios
from database import engine, Base
from App.routes import auth


# Si ya creaste las tablas manualmente, puedes omitir esta línea
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Api para guardar PROYECTOS",
    description="CRUD para gestionar proyectos del portafolio personal",
    version="1.0.0"
)
app.include_router(auth.router)

# Registrar las rutas del módulo proyectos
app.include_router(proyecto.router)
app.include_router(categorias.router)
app.include_router(comentarios.router)



#@app.get('/')
#def read_root():
#    return {"welcome": "Welcome to my API"}