from pydantic import model_validator
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

    # Identity & Access (LDMS-009/010/018)
    auth_mode: str = "mock"  # "mock" | "google"
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expires_minutes: int = 60
    google_client_id: str | None = None
    google_client_secret: str | None = None
    google_redirect_uri: str | None = None
    google_allowed_domains: list[str] = ["hcmus.edu.vn"]
    frontend_base_url: str = "http://localhost:5173"

    @model_validator(mode="after")
    def _validate_google_mode(self) -> "Settings":
        if self.auth_mode == "google" and not (
            self.google_client_id and self.google_client_secret and self.google_redirect_uri
        ):
            raise ValueError(
                "AUTH_MODE=google requires GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "
                "GOOGLE_REDIRECT_URI to be set."
            )
        return self


settings = Settings()
