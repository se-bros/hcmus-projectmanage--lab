from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Required env vars have no default: missing one fails fast at startup (LDMS-001 AC4)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = "development"
    database_url: str

    @field_validator("database_url", mode="before")
    @classmethod
    def normalize_database_url(cls, v: str) -> str:
        if isinstance(v, str):
            if v.startswith("postgres://"):
                return "postgresql+psycopg://" + v[len("postgres://") :]
            if v.startswith("postgresql://") and not v.startswith("postgresql+"):
                return "postgresql+psycopg://" + v[len("postgresql://") :]
        return v
    @field_validator("cors_origins", mode="before")
    @classmethod
    def normalize_cors_origins(cls, v: object) -> list[str]:
        if isinstance(v, str):
            v_str = v.strip()
            if v_str.startswith("[") and v_str.endswith("]"):
                import json

                try:
                    return json.loads(v_str)
                except Exception:
                    pass
            return [origin.strip() for origin in v_str.split(",") if origin.strip()]
        if isinstance(v, list):
            return [str(origin) for origin in v]
        return ["http://localhost:5173"]

    minio_endpoint: str
    minio_access_key: str
    minio_secret_key: str
    minio_bucket: str = "ldms"
    minio_secure: bool = False
    cors_origins: list[str] = ["http://localhost:5173", "https://hcmus-projectmanage-lab.vercel.app"]
    ocr_dpi: int = 300
    ocr_language: str = "vie+eng"
    ocr_timeout_seconds: int = 60
    pdf_render_timeout_seconds: int = 120
    pandoc_timeout_seconds: int = 120

    # Identity & Access (LDMS-009/010/018)
    enable_mock_auth: bool = True
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expires_minutes: int = 60
    google_client_id: str | None = None
    google_client_secret: str | None = None
    google_redirect_uri: str | None = None
    # Empty list = no domain restriction (any email allowed) for register + Google login.
    google_allowed_domains: list[str] = []
    frontend_base_url: str = "http://localhost:5173"


settings = Settings()
