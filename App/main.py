from fastapi import FastAPI
from App.routes import proyecto, categorias, comentarios
from database import engine, Base
from App.routes import auth
from fastapi.middleware.cors import CORSMiddleware


# Si ya creaste las tablas manualmente, puedes omitir esta línea
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Api para guardar PROYECTOS",
    description="CRUD para gestionar proyectos del portafolio personal",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a mi API REST con FastAPI! Ve a /docs para ver la documentación 📚"}


app.include_router(auth.router)

# Registrar las rutas del módulo proyectos
app.include_router(proyecto.router)
app.include_router(categorias.router)
app.include_router(comentarios.router)


#CORS 
origins = [
    "http://localhost:5173",      # Vite
    "http://127.0.0.1:5173"
    #"https://TU-FRONTEND-DOMINIO" # cuando lo despliegues
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)


#@app.get('/')
#def read_root():
#    return {"welcome": "Welcome to my API"}