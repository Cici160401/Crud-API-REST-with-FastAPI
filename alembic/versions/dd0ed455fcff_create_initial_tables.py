"""create initial tables

Revision ID: dd0ed455fcff
Revises: 
Create Date: 2025-07-29 19:33:27.875091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd0ed455fcff'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_index(op.f('ix_categorias_id'), 'categorias', ['id'], unique=False)
    op.create_table('proyectos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=False),
    sa.Column('tecnologias', sa.Text(), nullable=False),
    sa.Column('url_repo', sa.String(length=255), nullable=True),
    sa.Column('url_demo', sa.String(length=255), nullable=True),
    sa.Column('imagen', sa.String(length=255), nullable=True),
    sa.Column('estado', sa.Enum('terminado', 'en_proceso', name='estadoproyecto'), nullable=False),
    sa.Column('destacado', sa.Boolean(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proyectos_id'), 'proyectos', ['id'], unique=False)
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('es_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuarios_id'), 'usuarios', ['id'], unique=False)
    op.create_table('comentarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proyecto_id', sa.Integer(), nullable=False),
    sa.Column('autor', sa.String(length=100), nullable=True),
    sa.Column('contenido', sa.Text(), nullable=False),
    sa.Column('fecha', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['proyecto_id'], ['proyectos.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comentarios_id'), 'comentarios', ['id'], unique=False)
    op.create_table('proyecto_categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proyecto_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['proyecto_id'], ['proyectos.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proyecto_categoria_id'), 'proyecto_categoria', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proyecto_categoria_id'), table_name='proyecto_categoria')
    op.drop_table('proyecto_categoria')
    op.drop_index(op.f('ix_comentarios_id'), table_name='comentarios')
    op.drop_table('comentarios')
    op.drop_index(op.f('ix_usuarios_id'), table_name='usuarios')
    op.drop_table('usuarios')
    op.drop_index(op.f('ix_proyectos_id'), table_name='proyectos')
    op.drop_table('proyectos')
    op.drop_index(op.f('ix_categorias_id'), table_name='categorias')
    op.drop_table('categorias')
    # ### end Alembic commands ###
