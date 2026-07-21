import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import ConflictError, ForbiddenError, UnauthorizedError
from app.db.base import Base
from app.models.user import User
from app.services import auth_service


@pytest.fixture(autouse=True)
def _allowed_domains(monkeypatch):
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])


def _db() -> Session:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return Session(engine)


def test_register_local_user_creates_reader_with_hashed_password():
    with _db() as db:
        user = auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        assert user.role == "reader"
        assert user.auth_provider == "local"
        assert user.password_hash != "supersecret"


def test_register_local_user_rejects_disallowed_domain():
    with _db() as db:
        with pytest.raises(ForbiddenError):
            auth_service.register_local_user(db, "student@gmail.com", "supersecret")


def test_register_local_user_rejects_duplicate_email():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        with pytest.raises(ConflictError):
            auth_service.register_local_user(db, "student@hcmus.edu.vn", "anotherpass")


def test_authenticate_local_user_accepts_correct_password():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        user = auth_service.authenticate_local_user(db, "student@hcmus.edu.vn", "supersecret")
        assert user.email == "student@hcmus.edu.vn"


def test_authenticate_local_user_rejects_wrong_password():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        with pytest.raises(UnauthorizedError):
            auth_service.authenticate_local_user(db, "student@hcmus.edu.vn", "wrongpass")


def test_authenticate_local_user_rejects_unknown_email():
    with _db() as db:
        with pytest.raises(UnauthorizedError):
            auth_service.authenticate_local_user(db, "nobody@hcmus.edu.vn", "supersecret")


def test_authenticate_local_user_rejects_google_only_account():
    with _db() as db:
        auth_service.find_or_create_google_user(db, "student@hcmus.edu.vn")
        with pytest.raises(UnauthorizedError):
            auth_service.authenticate_local_user(db, "student@hcmus.edu.vn", "anything")


def test_find_or_create_google_user_creates_reader_first_time():
    with _db() as db:
        user = auth_service.find_or_create_google_user(db, "student@hcmus.edu.vn")
        assert user.role == "reader"
        assert user.auth_provider == "google"
        assert user.password_hash is None


def test_find_or_create_google_user_reuses_existing_local_identity():
    with _db() as db:
        local_user = auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        google_user = auth_service.find_or_create_google_user(db, "student@hcmus.edu.vn")
        assert google_user.id == local_user.id
        assert google_user.auth_provider == "local"


def test_check_allowed_domain_rejects_non_allowed_domain():
    with pytest.raises(ForbiddenError):
        auth_service.check_allowed_domain("someone@gmail.com")


def test_check_allowed_domain_accepts_allowed_domain():
    auth_service.check_allowed_domain("someone@hcmus.edu.vn")  # does not raise


def test_registered_user_is_queryable_by_email():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        assert db.scalar(select(User).where(User.email == "student@hcmus.edu.vn")) is not None
