import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Stock Market app"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("DB_USER")
    POSTGRES_PASSWORD = os.getenv("DB_PASS")
    POSTGRES_SERVER: str = os.getenv("DB_HOST")
    POSTGRES_PORT: str = os.getenv("DB_PORT", 5432)
    POSTGRES_DB: str = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()