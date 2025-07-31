# utils.py
#EN ESTA CLASE VAMOS A HASHEAR LA CONTRASEÑA

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)



