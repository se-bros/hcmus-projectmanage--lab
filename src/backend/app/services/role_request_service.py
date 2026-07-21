import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, ForbiddenError, NotFoundError
from app.models.role_request import RoleRequest
from app.models.user import User

REQUESTABLE_ROLE = "editor"


def create_role_request(db: Session, requester: User) -> RoleRequest:
    if requester.role != "reader":
        raise ForbiddenError("Only readers can request editor access.")
    existing = db.scalar(
        select(RoleRequest).where(
            RoleRequest.user_id == requester.id, RoleRequest.status == "pending"
        )
    )
    if existing is not None:
        raise ConflictError("You already have a pending request.")

    request = RoleRequest(
        id=uuid.uuid4(),
        user_id=requester.id,
        requested_role=REQUESTABLE_ROLE,
        status="pending",
    )
    db.add(request)
    db.commit()
    db.refresh(request)
    return request


def get_latest_request_for_user(db: Session, user_id: uuid.UUID) -> RoleRequest | None:
    return db.scalar(
        select(RoleRequest)
        .where(RoleRequest.user_id == user_id)
        .order_by(RoleRequest.created_at.desc())
        .limit(1)
    )


def list_role_requests(db: Session) -> list[RoleRequest]:
    return list(db.scalars(select(RoleRequest).order_by(RoleRequest.created_at.desc())))


def decide_role_request(
    db: Session, request_id: uuid.UUID, approve: bool, admin_id: uuid.UUID
) -> RoleRequest:
    request = db.get(RoleRequest, request_id)
    if request is None:
        raise NotFoundError("Role request not found.")
    if request.status != "pending":
        raise ConflictError("Role request has already been decided.")

    request.status = "approved" if approve else "rejected"
    request.decided_at = datetime.now(UTC)
    request.decided_by = admin_id
    if approve:
        target_user = db.get(User, request.user_id)
        if target_user is not None:
            target_user.role = request.requested_role
    db.commit()
    db.refresh(request)
    return request
