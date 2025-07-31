from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from App.config import settings
from typing import Union
from sqlalchemy.orm import Session
from App.auth.jwt_handler import decode_access_token
from App.models.usuarios import Usuario
from database import get_db


# En esta clase definimos las funciones de autenticación automática que puedo usar como dependencia en mis rutas
#---Ejemplo: get_current_user --> toma el token de usuario, lo verifica y retorna el usuario si es válido.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

#Esta función depende de que el usuario dé un token, si no, fastapi responde que necesita autenticarse
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Union[Usuario, dict]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        if payload is None:
            raise credentials_exception

        username: str = payload.get("sub")
        role: str = payload.get("role", "user")  # ← nuevo

        if username is None:
            raise credentials_exception

        # ✔ Si es invitado, devolvemos un dict especial (sin acceder a la DB)
        if role == "guest":
            #return {"username": "guest", "role": "guest"}
            return Usuario(username="guest", email="guest@example.com", es_admin=False)

        # ✔ Usuarios reales
        user = db.query(Usuario).filter(Usuario.username == username).first()
        if user is None:
            raise credentials_exception

        print(f"Usuario autenticado: {user.username}")
        return user

    except JWTError:
        raise credentials_exception
    

