from datetime import datetime,timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Optional
from App.config import settings

#clase para crear y decodificar tokens JWT (JSON WEB TOKEN)

#--ciframos contraseñas con passlib
#--generando un token de acceso con create_access_token
#--decodificando ese token con decode_access_token


#se importa datetime para generar la expiración del token
#jose: Librería que permite crear y verificar tokens JWT.
#jwt: Permite codificar (encode) y decodificar (decode) tokens.

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
EXPIRATION_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

#Configuración del hash de contraseñas
#bcrypt es un algoritmo de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")

def hash_password(password : str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    #data: Es un diccionario que representa la información del usuario.
    to_encode = data.copy()
    #expires_delta: Puede pasarle manualmente el tiempo de expiración (si no, se usa el valor por defecto).
    expire = datetime.now() + (expires_delta or timedelta(minutes=EXPIRATION_MINUTES))

    #exp: Campo estándar en JWT que define cuándo el token expira y establece el sub (viene de subjet),
    #que es como le denominaremos al nombre de usuario 
    #incluimos el rol en el payload del token cuando se genera
    to_encode.update({
        "exp": expire,
        "sub": data["sub"],
        "role": data.get("role", "user")  # ← asigna "user" si no se pasa rol
    })
     
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_access_token(token: str):
    try:
        #decode: Desencripta el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Payload decodificado:", payload) 
        #Devuelve la data
        return payload
    except JWTError as e:
        print("Error al decodificar token:", e)
        return None