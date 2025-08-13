from __future__ import annotations
import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from dotenv import load_dotenv

# --- Carga de .env solo en local/test ---
ENV = os.getenv("ENV")
if ENV == "test":
    load_dotenv(".env.test")
else:
    if os.path.exists(".env"):     # en Render normalmente no existe
        load_dotenv(".env")

# --- Helpers ---
def _coerce_mysql_driver(url: str | None) -> str | None:
    """Si viene mysql:// lo convierte a mysql+pymysql:// para SQLAlchemy."""
    if not url:
        return url
    if url.startswith("mysql://"):
        return "mysql+pymysql://" + url[len("mysql://"):]
    return url

def get_database_url() -> str:
    # 1) Producción: usa DATABASE_URL si existe
    url = os.getenv("DATABASE_URL")
    if url:
        return _coerce_mysql_driver(url)

    # 2) Local/CI: arma la URL con variables separadas
    user = os.getenv("DB_USER", "root")
    pwd  = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "3306")
    name = os.getenv("DB_NAME", "portafolio")
    return f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{name}"

DATABASE_URL = get_database_url()
print(f"\n[DEBUG] DATABASE_URL = {DATABASE_URL}\n", flush=True)

# --- Engine y sesión ---
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # reconecta si la conexión quedó dormida
    pool_recycle=1800,    # recicla cada 30 min
    future=True
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()

# --- Dependencia FastAPI ---
def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()