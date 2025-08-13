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
# --- CORS ---
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Agrega aquí el dominio real de tu frontend cuando lo despliegues:
    # "https://tu-frontend.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # <-- permite cualquier origen
    allow_credentials=False,    # <-- obligatorio si usas "*"
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- CORS ---
@app.get("/")
def read_root():
    return {"message": "¡Bienvenido a mi API REST con FastAPI! Ve a /docs para ver la documentación 📚"}


app.include_router(auth.router)

# Registrar las rutas del módulo proyectos
app.include_router(proyecto.router)
app.include_router(categorias.router)
app.include_router(comentarios.router)



#@app.get('/')
#def read_root():
#    return {"welcome": "Welcome to my API"}