from sqlalchemy.orm import Session
from typing import List, Optional
from App.models import Proyecto
from App.models.categorias import Categoria
from App.models.proyecto import EstadoProyecto
from App.schemas.proyecto import ProyectoCreate, ProyectoUpdate
from sqlalchemy import or_


#Crear un nuevo proyecto

def crear_proyecto(db: Session, proyecto: ProyectoCreate):
    print("RECIBIDO:", proyecto)
    #proyecto es una instancia del modelo PYDANTIC: ProyectoCreate
    #.modeldump() -> convierte ese modelo en un diccionario 
    #Usamos ** para desempaquetar el diccionario y pasarlo como argumentos a Proyecto(...)
    #nuevo = Proyecto(**proyecto.model_dump())
    nuevo = Proyecto(
        nombre=proyecto.nombre,
        descripcion=proyecto.descripcion,
        tecnologias=proyecto.tecnologias,
        url_repo=proyecto.url_repo,
        url_demo=proyecto.url_demo,
        imagen=proyecto.imagen,
        estado=proyecto.estado,
        destacado=proyecto.destacado
    )

    if proyecto.categorias_ids:
        categorias = db.query(Categoria).filter(Categoria.id.in_(proyecto.categorias_ids)).all()
        nuevo.categorias = categorias

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Listar proyectos
def listar_proyectos(db: Session) -> List[Proyecto]:
    return Proyecto

# Buscar por nombre

def obtener_proyectos(db: Session , search: Optional[str] = None) -> List[Proyecto]:
    query = db.query(Proyecto)
    if search:        
        query = query.filter(Proyecto.nombre.ilike(f"%{search}%"))
    return query.order_by(Proyecto.fecha_creacion.desc()).all()

# Obtener proyecto por ID

def obtener_proyecto_por_id(db: Session, proyecto_id : int) -> Optional[Proyecto]:
    return db.query(Proyecto).filter(Proyecto.id == proyecto_id ).first()

# Actualizar un proyecto por ID

def actualizar_proyecto_db(db: Session, proyecto_id: int, cambios : ProyectoUpdate):
    proyecto= obtener_proyecto_por_id(db, proyecto_id)
    if not proyecto:
        return None
    # Iteramos sobre los campos que el usuario envió
    for campo, valor in cambios.model_dump(exclude_unset=True).items():
        #Establecemos el valor de un atributo a un objeto
        #Objeto, Atributo, Valor
        setattr(proyecto,campo,valor)
    db.commit()
    db.refresh(proyecto)
    return proyecto

def eliminar_proyecto(db: Session, proyecto_id: int):
    proyecto = obtener_proyecto_por_id(db, proyecto_id)
    if proyecto: 
        db.delete(proyecto)
        db.commit()
    return proyecto
