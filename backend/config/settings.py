from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    OPENAI_API_KEY: str

    DATABASE_URL: str

    LOG_LEVEL: str

    CONFIDENCE_THRESHOLD: float

    MAX_UPLOAD_SIZE_MB: int
        
    OPENAI_MODEL: str = "gpt-5.5"
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()