from pydantic import BaseModel, HttpUrl
from typing import Optional, Literal, List
from datetime import datetime
from App.schemas.categorias import Categoria
from App.models.proyecto import EstadoProyecto


#Base común para heredar campos. Evita repetirlos.
class ProyectoBase (BaseModel):
    nombre: str
    descripcion: str
    tecnologias: str
    url_repo: Optional[HttpUrl] = None
    url_demo: Optional[HttpUrl] = None
    imagen: Optional[HttpUrl] = None
    #estado: EstadoProyecto
    estado: EstadoProyecto = EstadoProyecto.en_proceso
    destacado: bool = False
    categorias: List[Categoria] = []

#Se usa al crear un proyecto (POST). Hereda de Base
class ProyectoCreate(ProyectoBase):
    categorias_ids: Optional[List[int]] = []  # <-- este campo nuevo

#Se usa al mostrar un proyecto (GET). Agrega ID, fecha.
class Proyecto(ProyectoBase):
    id: int 
    fecha_creacion: datetime

    class Config:
        from_attributes = True
        use_enum_values = True

# Schema para actualizar
class ProyectoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    tecnologias: Optional[str] = None
    url_repo: Optional[HttpUrl] = None
    url_demo: Optional[HttpUrl] = None
    imagen: Optional[HttpUrl] = None
    estado: Optional[Literal["terminado", "en_proceso"]] = None
    destacado: Optional[bool] = None
    categorias_ids: Optional[List[int]] = []