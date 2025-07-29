from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
#from database import Base
from App.models.base import Base

class Comentario(Base):
    __tablename__="comentarios"

    id = Column(Integer, primary_key=True, index=True)
    proyecto_id= Column(Integer, ForeignKey("proyectos.id", ondelete="CASCADE"), nullable= False)
    autor = Column(String(100), nullable=True)
    contenido = Column(Text, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())

    #relationship()	Crea una relación entre modelos.
    #back_populates	Crea la relación en ambos sentidos y las mantiene sincronizadas.
    #Establecemos una relación para poder listar los comentarios de x proyecto
    proyecto= relationship("Proyecto", back_populates="comentarios")


