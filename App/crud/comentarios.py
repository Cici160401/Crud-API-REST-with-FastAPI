from sqlalchemy.orm import Session
from App.models.comentarios import Comentario
from App.schemas.comentarios import ComentarioCreate
from typing import List, Optional

#Crear nuevo comentario
def crear_comentario(db: Session, comentario: ComentarioCreate):
    nuevo_comentario = Comentario(**comentario.model_dump())
    db.add(nuevo_comentario)
    db.commit()
    db.refresh(nuevo_comentario)
    return nuevo_comentario

#Listar todos los comentarios
def listar_comentarios(db: Session)-> List[Comentario]:        
    query= db.query(Comentario)    
    return query.all()

#Listar comentarios por proyectos
def listar_comentarios_por_proyecto(db: Session, proyecto_id: int) -> List[Comentario]:
    return db.query(Comentario).filter(Comentario.proyecto_id == proyecto_id).all()

#Listar comentarios por id
def listar_comentarios_por_id(db: Session, comentario_id: int) -> Optional[Comentario]:
    return db.query(Comentario).filter(Comentario.id == comentario_id).first()

#Eliminar comentario
def eliminar_comentario(db: Session, comentario_id: int):
    comentario = db.query(Comentario).filter(Comentario.id == comentario_id).first()
    if comentario :
        datos = comentario
        db.delete(comentario)
        db.commit()
        #db.refresh(comentario)
        return datos
    return None