from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context

# Alembic Config object
config = context.config
print("DEBUG: ¡Alembic está cargando ESTE env.py!")

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa tus modelos para que Alembic detecte las tablas
from App.models.base import Base  
from App.models import proyecto, comentarios, categorias, proyecto_categoria, usuarios

# Asegura que todas las tablas estén registradas
target_metadata = Base.metadata
print(f"DEBUG: Tablas registradas en target_metadata: {list(target_metadata.tables.keys())}")

# Usa tu función personalizada para obtener la URL de conexión
from database import get_database_url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    db_url = get_database_url()
    print(f"DEBUG: URL de la base de datos usada por Alembic: {db_url}")

    connectable = create_engine(
        db_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        # 🔥 Aquí es donde antes fallaba — SIEMPRE ejecutamos run_migrations
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
