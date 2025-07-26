#from passlib.context import CryptContext

#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#hashed = pwd_context.hash("admin")
#print(hashed)
#import httpx

#Estoy usando JWT con OAuth2PasswordBearer para implementar autenticación basada en tokens. 
# Mis rutas protegidas dependen de un get_current_user() que extrae el token del encabezado, 
# lo decodifica, verifica su validez, y devuelve al usuario. Además, uso pydantic.BaseSettings
#  para cargar las variables sensibles desde un .env, como la clave secreta y el tiempo de expiración.
#  Esto asegura que solo usuarios autenticados puedan acceder a rutas protegidas, y puedo controlar 
# cuánto dura la sesión con precisión. Todo está implementado con FastAPI siguiendo buenas prácticas de seguridad.

#print(httpx.__version__)