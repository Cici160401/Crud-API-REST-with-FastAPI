from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Response
from typing import List, Optional
from App.schemas.categorias import Categoria, CategoriaCreate, CategoriaUpdate
from App.auth.dependencies import get_current_user
from App.models.usuarios import Usuario
from App.crud.categorias import (
    crear_categoria,
    obtener_categorias,
    obtener_categorias_por_id,
    actualizar_categoria_db,
    eliminar_categoria
)
router = APIRouter (
    prefix="/categorias",
    tags=["Categorias"]
)

#Listar Categorias o Buscar por nombre
@router.get("/", response_model= List[Categoria])
def listar_categorias(
    search: Optional[str]= Query(None, description= "Buscar por nombre"),
    db: Session = Depends(get_db)
    ):
    return obtener_categorias(db = db, search=search)

#Obtener categorias por ID
@router.get("/{categoria_id}",response_model=Categoria)
def ver_categoria(categoria_id : int, db: Session= Depends(get_db)):
    categoria = obtener_categorias_por_id(db, categoria_id)
    if not categoria:
        #si la categoría no existe, se lanza una excepcion
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    return categoria

#Creamos una categoria
@router.post("/",response_model=Categoria)
def crear_nueva_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db), user : Usuario=Depends(get_current_user)):
    print("Usuario autenticado:", user.username)
    return crear_categoria(db=db,categoria=categoria)

#Eliminamos la categoria
#@router.delete("/{categoria_id}",status_code=204)
#def borrar_categoria(categoria_id: int, db: Session = Depends(get_db), user : Usuario=Depends(get_current_user)):
#    categoria = eliminar_categoria(db, categoria_id)
#    if not categoria :
#        raise HTTPException(status_code=404,detail="Categoria no existe, no se puede eliminar")
#    return Response(status_code=204)

@router.delete("/{categoria_id}", status_code=200, response_model=dict)
def borrar_categoria(
    categoria_id: int,
    db: Session = Depends(get_db),
    user: Usuario = Depends(get_current_user)
):
    categoria = eliminar_categoria(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no existe, no se puede eliminar")
    return {"mensaje": "Categoría eliminada con éxito"}

#Actualizamos mi categoría
@router.put("/{categoria_id}", response_model=Categoria)
def actualizar_categoria(categoria_id: int, cambios: CategoriaUpdate,db : Session = Depends(get_db), user: Usuario = Depends(get_current_user)):
    categoria = actualizar_categoria_db(db, categoria_id, cambios)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrada, no se puede actualizar")
    return categoria