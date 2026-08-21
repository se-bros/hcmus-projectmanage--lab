from datetime import timedelta

from minio import Minio

from app.core.config import settings

minio_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=settings.minio_secure,
)


def ensure_bucket_exists() -> None:
    if not minio_client.bucket_exists(settings.minio_bucket):
        minio_client.make_bucket(settings.minio_bucket)


def get_presigned_url(object_key: str, expires_seconds: int = 900) -> str:
    return minio_client.presigned_get_object(
        settings.minio_bucket, object_key, expires=timedelta(seconds=expires_seconds)
    )
