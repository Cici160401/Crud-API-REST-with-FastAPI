from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

env_file = ".env.test" if os.getenv("USE_TEST_ENV") == "1" else ".env"
load_dotenv(dotenv_path=env_file)

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"

# Creamos una instancia para usarla donde se necesite
settings = Settings()
print("DEBUG CONFIG: ", settings.SECRET_KEY, settings.ACCESS_TOKEN_EXPIRE_MINUTES)