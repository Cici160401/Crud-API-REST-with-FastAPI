from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

# SOLO cargar dotenv si estás en local
if os.path.exists(".env") or os.path.exists(".env.test"):
    from dotenv import load_dotenv
    env_file = ".env.test" if os.getenv("ENV") == "test" else ".env"
    load_dotenv(dotenv_path=env_file)
    
# Cargar variables desde el archivo .env
#load_dotenv()

# Recuperar datos desde .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")


# Construir URL de conexión a MySQL
def get_database_url():
    return f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear el engine para SQLAlchemy
engine = create_engine(get_database_url())

# Crear la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para declarar los modelos
Base = declarative_base()

# Dependencia para obtener la sesión
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


