from sqlalchemy import Column, Integer, String, Boolean
#from database import Base
from App.models.base import Base

class Usuario(Base):
    __tablename__= "usuarios"

    id= Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    es_admin = Column(Boolean, default=False)
    



