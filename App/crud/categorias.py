from sqlalchemy.orm import Session
from App.models.categorias import Categoria
from App.schemas.categorias import CategoriaCreate, CategoriaUpdate
from typing import List, Optional

# Crear nueva categoría

def crear_categoria(db: Session, categoria: CategoriaCreate):
    nueva_categoria = Categoria(nombre=categoria.nombre)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

# Listar categorías
#Vamos a establecer como argumentos la sesión y también una búsqueda Opcional, la estableceremos como None por si no hacen ninguna búsqueda
#
def obtener_categorias(db: Session, search: Optional[str] = None)-> List[Categoria]:        
    query= db.query(Categoria)
    if search:
        query= query.filter(Categoria.nombre.ilike(f"%{search}%"))
    return query.all()


#Obtener categoría por Id

def obtener_categorias_por_id(db: Session, categoria_id: int) -> Optional[Categoria]:
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

#Actualizar categoría

def actualizar_categoria_db(db: Session, categoria_id : int, cambios: CategoriaUpdate):
    categoria= obtener_categorias_por_id(db, categoria_id)
    if not categoria:
        return None    
    # Actualiza solo los campos que llegaron en cambios (por ahora solo 'nombre')
    categoria.nombre = cambios.nombre
    db.commit()
    db.refresh(categoria)
    return categoria

#Eliminar categoría
 
def eliminar_categoria(db: Session, categoria_id : int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
        #db.refresh(categoria)
    return categoria






