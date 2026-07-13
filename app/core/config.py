from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str

    database_url: str

    redis_host: str
    redis_port: int
    redis_password: str

    celery_broker_url: str
    celery_result_backend: str

    tz: str = "UTC"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()
