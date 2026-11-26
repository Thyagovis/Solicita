from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

BASE_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):

    ai_api_key : SecretStr

    model_config = SettingsConfigDict(
        env_file= BASE_DIR /".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
