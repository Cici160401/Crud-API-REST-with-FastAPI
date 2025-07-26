from pydantic import BaseModel
from datetime import datetime
from typing import Optional 

class ComentarioBase (BaseModel):
    autor: str
    contenido: str

class ComentarioCreate (ComentarioBase):
    proyecto_id: int

class Comentario (ComentarioBase):
    id: int
    proyecto_id : int
    fecha : datetime
    
    class Config:
        from_attributes= True
