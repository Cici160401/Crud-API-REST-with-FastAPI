from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi import Response
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from App.schemas.proyecto import Proyecto, ProyectoCreate, ProyectoUpdate
from App.auth.dependencies import get_current_user
from App.models.usuarios import Usuario
from App.crud.proyecto import (
    crear_proyecto,
    obtener_proyectos,
    obtener_proyecto_por_id,
    actualizar_proyecto_db,
    eliminar_proyecto
)

router = APIRouter(
    prefix="/proyectos",
    tags=["Proyectos"]
)
#Listar proyectos
#@router.get("/listar", response_model=List[Proyecto])
#def listar_proyectos(db: Session = Depends(get_db)
#    ):
#    return obtener_proyectos(db=db)

#Buscar por nombre
@router.get("/", response_model=List[Proyecto])
def listar_proyectos(
    search: Optional[str] = Query(None, description="Buscar por nombre"),
    db: Session = Depends(get_db)
    ):
    return obtener_proyectos(db=db,search=search)
    
#Obtener un proyecto por ID
@router.get("/{proyecto_id}", response_model=Proyecto)
def ver_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    proyecto = obtener_proyecto_por_id(db, proyecto_id)
    if not proyecto:
        #Si el proyecto no existe, se lanza una excepción
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

#Creamos nuevo proyecto
@router.post("/", response_model=Proyecto)
def crear_nuevo_proyecto(proyecto: ProyectoCreate,db: Session = Depends(get_db),user: Usuario =Depends(get_current_user)):
    #if user.rol != "admin":
        #raise HTTPException(status_code=403, detail="Solo los admins pueden crear proyectos")
    print("Usuario autenticado:", user.username)
    return crear_proyecto(db =db,proyecto=proyecto)

#Eliminamos un proyecto
@router.delete("/{proyecto_id}",status_code=204)
def borrar_proyecto(proyecto_id: int,db: Session = Depends(get_db),user: Usuario =Depends(get_current_user)):
    proyecto = eliminar_proyecto(db, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no existe, no se puede borrar")
    return Response(status_code=204)

#Actualizamos un proyecto
@router.put("/{proyecto_id}", response_model=Proyecto)
def actualizar_proyecto(proyecto_id: int, cambios: ProyectoUpdate, db: Session = Depends(get_db),user: Usuario =Depends(get_current_user)):
    proyecto = actualizar_proyecto_db(db, proyecto_id, cambios)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado, no se puede actualizar")
    return proyecto

