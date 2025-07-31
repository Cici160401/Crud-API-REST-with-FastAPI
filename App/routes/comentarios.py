from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi import Response
from sqlalchemy.orm import Session
from database import get_db
from typing import List, Optional
from App.auth.dependencies import get_current_user
from App.models.usuarios import Usuario
#TUVE QUE ESTABLECER UN ALIAS PORQUE EL SCHEMA Y EL MODEL TENÍAN EL MISMO NOMBRE, ENTONCES DABA ERRORES DE FORMATO
from App.models.comentarios import Comentario as ComentarioModel
from App.schemas.comentarios import Comentario, ComentarioCreate 
from App.crud.comentarios import (
    crear_comentario,
    listar_comentarios_por_proyecto,
    listar_comentarios_por_id,
    listar_comentarios,
    eliminar_comentario
)


router = APIRouter (
    prefix="/comentarios",
    tags=["Comentarios"]
)
# RUTA POST PARA CREAR COMENTARIO
@router.post("/", response_model=Comentario)
def crear_nuevo_comentario(
    comentario: ComentarioCreate,
    db: Session = Depends(get_db),
    user: Usuario = Depends(get_current_user)  # ahora acepta guest también
):
     # Asignamos autor automáticamente desde el token creado en /login/guest
    autor = user.username #if hasattr(user, "username") else user.get("username", "Invitado")
    
     # Creamos una copia del comentario con autor incluido
    comentario_dict = comentario.model_dump()
    comentario_dict["autor"] = autor
    nuevo_comentario = ComentarioCreate(**comentario_dict)

    # Guardamos el comentario
    return crear_comentario(db, nuevo_comentario)

#RUTA GET PARA LISTAR LOS COMENTARIOS DE UN PROYECTO
@router.get("/proyectos/{proyecto_id}",response_model=List[Comentario])
def obtener_comentarios_por_proyecto(proyecto_id: int, db : Session = Depends(get_db)):
    return listar_comentarios_por_proyecto(db, proyecto_id)

#RUTA GET PARA LISTAR TODOS LOS COMENTARIOS
@router.get("/", response_model=List[Comentario])
def listar_todos_los_comentarios(db: Session = Depends(get_db)):
    return listar_comentarios(db)

#RUTA GET PARA OBTENER COMENTARIOS POR ID
@router.get("/{comentario_id}", response_model=Optional[Comentario])
def obtener_comentario_por_id(comentario_id: int, db: Session = Depends(get_db)):
    comentario = listar_comentarios_por_id(db, comentario_id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return comentario

#RUTA DELETE PARA ELIMINAR UN COMENTARIO
@router.delete("/{comentario_id}", status_code=204)
def borrar_comentario(comentario_id: int, db: Session = Depends(get_db), user: Usuario = Depends(get_current_user)):
    comentario = eliminar_comentario(db, comentario_id)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado o ya eliminado")
    return Response(status_code=204)

