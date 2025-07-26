from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from App.models.usuarios import Usuario
from App.auth.jwt_handler import create_access_token, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

@router.post("/login")
#form_data: Extrae automáticamente username y password
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Busca en la base de datos al usuario con ese username.
    user = db.query(Usuario).filter(Usuario.username == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )

    #genera un token JWT con el campo "sub" (subject) igual al username.
    #Retorna un diccionario con el access_token, que será usado en las siguientes peticiones como autenticación.

    #Si existiera roles para los usuarios, aquí se declararía: data={"sub": user.username, "rol": user.rol}
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}