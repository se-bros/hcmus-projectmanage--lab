import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import ConflictError, ForbiddenError, UnauthorizedError
from app.core.security import hash_password, verify_password
from app.models.user import User

DEFAULT_ROLE = "reader"


def check_allowed_domain(email: str) -> None:
    if not any(email.lower().endswith(f"@{domain}") for domain in settings.google_allowed_domains):
        allowed = ", ".join(f"@{domain}" for domain in settings.google_allowed_domains)
        raise ForbiddenError(f"Only {allowed} accounts are allowed.")


def register_local_user(db: Session, email: str, password: str) -> User:
    check_allowed_domain(email)
    if db.scalar(select(User).where(User.email == email)) is not None:
        raise ConflictError("An account with this email already exists.")
    user = User(
        id=uuid.uuid4(),
        email=email,
        password_hash=hash_password(password),
        role=DEFAULT_ROLE,
        auth_provider="local",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_local_user(db: Session, email: str, password: str) -> User:
    user = db.scalar(select(User).where(User.email == email))
    if (
        user is None
        or user.password_hash is None
        or not verify_password(password, user.password_hash)
    ):
        raise UnauthorizedError("Invalid email or password.")
    return user


def find_or_create_google_user(db: Session, email: str, name: str | None = None) -> User:
    user = db.scalar(select(User).where(User.email == email))
    if user is not None:
        return user
    user = User(
        id=uuid.uuid4(),
        email=email,
        username=name,
        password_hash=None,
        role=DEFAULT_ROLE,
        auth_provider="google",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: str) -> User | None:
    try:
        return db.get(User, uuid.UUID(user_id))
    except ValueError:
        return None


def update_profile(db: Session, user: User, username: str | None) -> User:
    user.username = username
    db.commit()
    db.refresh(user)
    return user


def change_password(
    db: Session, user: User, current_password: str | None, new_password: str
) -> User:
    if user.password_hash is not None:
        if current_password is None or not verify_password(current_password, user.password_hash):
            raise UnauthorizedError("Current password is incorrect.")
    user.password_hash = hash_password(new_password)
    db.commit()
    db.refresh(user)
    return user
