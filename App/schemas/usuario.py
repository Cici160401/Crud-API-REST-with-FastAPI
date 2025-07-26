from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    username : str
    email : EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

#Es lo que devuelve los datos al frontend, son datos que no se ingresan, se crean automáticamente la bd
class Usuario(UsuarioBase):
    id: int
    es_admin: bool

    class Config:
        from_attributes = True


