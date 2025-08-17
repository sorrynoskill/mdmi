from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mdmi_env: str = Field(default="development", env="MDMI_ENV")
    database_url: str = Field(
        default="postgresql://localhost:5432/mdmi", env="DATABASE_URL"
    )
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")


settings = Settings()
