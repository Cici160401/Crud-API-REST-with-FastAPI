from sqlalchemy import Column, Integer, ForeignKey
from database import Base

class ProyectoCategoria(Base):
    __tablename__ = "proyecto_categoria"

    id = Column(Integer, primary_key=True, index=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id", ondelete="CASCADE"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="CASCADE"), nullable=False)