from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Union
import json

class Settings(BaseSettings):
    APP_NAME: str = "Gram Panchayat ERP API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "production"
    API_V1_STR: str = "/api/v1"
    
    DATABASE_URL: str
    REDIS_URL: str = "redis://localhost:6379/0"
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    BACKEND_CORS_ORIGINS: List[str] = []

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', case_sensitive=True)

settings = Settings()
