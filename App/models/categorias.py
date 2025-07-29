from sqlalchemy import Column, Integer, String
#from database import Base
from sqlalchemy.orm import relationship
from App.models.base import Base

class Categoria(Base):
    __tablename__="categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre= Column(String(100),unique=True, nullable= False)
    

    #Establecemos relación muchos a muchos entre categoría y proyecto
    proyectos = relationship("Proyecto",secondary="proyecto_categoria",back_populates="categorias")    


