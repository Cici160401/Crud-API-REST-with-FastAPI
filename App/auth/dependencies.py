from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from App.config import settings
from sqlalchemy.orm import Session
from App.auth.jwt_handler import decode_access_token
from App.models.usuarios import Usuario
from database import get_db


# En esta clase definimos las funciones de autenticación automática que puedo usar como dependencia en mis rutas
#---Ejemplo: get_current_user --> toma el token de usuario, lo verifica y retorna el usuario si es válido.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

#Esta función depende de que el usuario dé un token, si no, fastapi responde que necesita autenticarse
def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        #Si no hay token o es inválido, devolvemos esta excepción personalizada con un error 401 (no autorizado).
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        if payload is None:
            raise credentials_exception
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

        # Aquí buscamos al usuario completo en la base
        user = db.query(Usuario).filter(Usuario.username == username).first()
        if user is None:
            raise credentials_exception

        print(f"Usuario autenticado: {user.username}")
        return user

    except JWTError:
        raise credentials_exception
    

