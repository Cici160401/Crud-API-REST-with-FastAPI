from __future__ import annotations
import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from dotenv import load_dotenv

# Detectar Render (Render inyecta RENDER=true)
RUNS_IN_RENDER = os.getenv("RENDER") == "true"

# --- Carga de .env solo en local/test ---
ENV = os.getenv("ENV")
if ENV == "test":
    load_dotenv(".env.test")
elif not RUNS_IN_RENDER and os.path.exists(".env"):
    load_dotenv(".env")

def _coerce_mysql_driver(url: str | None) -> str | None:
    if not url:
        return url
    if url.startswith("mysql://"):
        return "mysql+pymysql://" + url[len("mysql://"):]
    return url

def get_database_url() -> str:
    # 1) Producción/Render: exige DATABASE_URL
    url = os.getenv("DATABASE_URL")
    if url:
        return _coerce_mysql_driver(url)
    if RUNS_IN_RENDER:
        # No permitas fallback a localhost en Render
        raise RuntimeError("DATABASE_URL no está definida en el entorno de Render")

    # 2) Local/CI: fallback a DB_*
    user = os.getenv("DB_USER", "root")
    pwd  = os.getenv("DB_PASSWORD", "")
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "3306")
    name = os.getenv("DB_NAME", "portafolio")
    return f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{name}"

DATABASE_URL = get_database_url()

# (Debug seguro: muestra host y base, no la password)
try:
    from urllib.parse import urlparse
    _u = urlparse(DATABASE_URL)
    print(f"[DEBUG] DB host={_u.hostname} port={_u.port} db={_u.path.lstrip('/')}", flush=True)
except Exception:
    pass

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800,
    future=True
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()