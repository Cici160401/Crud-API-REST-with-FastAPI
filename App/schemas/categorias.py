from pydantic import BaseModel

#Esquema base con campos comunes
class CategoriaBase(BaseModel):
    nombre: str

#Este es el esquema base con los campos comunes
class CategoriaCreate(CategoriaBase):
    pass 

# Schema para actualizar
class CategoriaUpdate(BaseModel):
    nombre: str #Definimos que solo el nombre será editable

#Para mostrar una categoría completa (incluye ID)
class Categoria(CategoriaBase):
    id: int
    #Permite que Pydantic convierta automáticamente los objetos provenientes de SQLAlchemy (ORM) a datos compatibles con los esquemas Pydantic
    class Config:
        from_attributes = True

    # SE DEBERÁ MIGRAR DE ESTA MANERA PORQUE EL CONFIG QUEDARÁ OBSOLETO EN PYDANTIC V2
    #class Proyecto(BaseModel):
    #model_config = ConfigDict(from_attributes=True)
    


