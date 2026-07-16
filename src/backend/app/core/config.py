from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Required env vars have no default: missing one fails fast at startup (LDMS-001 AC4)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    database_url: str
    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket: str = "ldms"
    cors_origins: list[str] = ["http://localhost:5173"]
    ocr_dpi: int = 300
    ocr_language: str = "vie+eng"
    ocr_timeout_seconds: int = 60
    pdf_render_timeout_seconds: int = 120
    pandoc_timeout_seconds: int = 120


settings = Settings()
