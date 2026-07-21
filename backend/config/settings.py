from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    # Gemini AI
    GEMINI_API_KEY: str
    GEMINI_MODEL: str

    # Database
    DATABASE_URL: str

    # Logging
    LOG_LEVEL: str

    # AI Settings
    CONFIDENCE_THRESHOLD: float

    # Upload Settings
    MAX_UPLOAD_SIZE_MB: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()