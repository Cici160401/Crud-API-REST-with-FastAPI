from sqlalchemy import Column, Integer, String, Text, Enum, Boolean, DateTime
from sqlalchemy.sql import func
#from database import Base
from App.models.base import Base
from sqlalchemy.orm import relationship
from App.models import proyecto_categoria
import enum


#Importamos func.now() para que MySQL cree la fecha de creación automáticamente.
#Importamos Base, que es la clase base para definir modelos SQLAlchemy.


#USAREMOS ENUM PARA EL ESTADO DEL PROYECTO, EN PROCESO O TERMINADO.
class EstadoProyecto(enum.Enum):
    terminado = "terminado"
    en_proceso = "en_proceso"

class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text,nullable=False)
    tecnologias = Column(Text,nullable= False)
    url_repo= Column(String(255))
    url_demo= Column(String(255))
    imagen = Column(String(255))
    estado = Column(Enum(EstadoProyecto), default=EstadoProyecto.en_proceso, nullable=False)
    destacado = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    
    #establecemos la relacion de muchos a muchos que tiene proyecto con categoria
    categorias = relationship("Categoria",secondary="proyecto_categoria",back_populates="proyectos")

    #relationship()	Crea una relación entre modelos.
    #back_populates	Crea la relación en ambos sentidos y las mantiene sincronizadas.
    #Le establecemos aqui una relacion inversa para poder listar los comentarios de un proyecto
    
    comentarios = relationship("Comentario", back_populates="proyecto", cascade="all, delete")

