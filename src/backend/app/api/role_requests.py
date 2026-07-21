"""Reader -> editor role upgrade requests, decided by admin."""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.dependencies import DbSession
from app.core.exceptions import NotFoundError
from app.core.security import AuthenticatedUser, get_current_user, require_roles
from app.models.role_request import RoleRequest
from app.schemas.role_request import RoleRequestDetail
from app.services import auth_service, role_request_service

router = APIRouter(prefix="/role-requests", tags=["role-requests"])


def _to_detail(request: RoleRequest) -> RoleRequestDetail:
    return RoleRequestDetail(
        id=str(request.id),
        user_id=str(request.user_id),
        user_email=request.user.email,
        user_username=request.user.username,
        requested_role=request.requested_role,
        status=request.status,
        created_at=request.created_at,
        decided_at=request.decided_at,
    )


@router.post("", response_model=RoleRequestDetail, status_code=201)
def create_request(
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> RoleRequestDetail:
    db_user = auth_service.get_user_by_id(db, user.sub)
    if db_user is None:
        raise NotFoundError("No account found for this session.")
    request = role_request_service.create_role_request(db, db_user)
    return _to_detail(request)


@router.get("/me", response_model=RoleRequestDetail | None)
def read_own_request(
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> RoleRequestDetail | None:
    db_user = auth_service.get_user_by_id(db, user.sub)
    if db_user is None:
        return None
    request = role_request_service.get_latest_request_for_user(db, db_user.id)
    return _to_detail(request) if request is not None else None


@router.get(
    "",
    response_model=list[RoleRequestDetail],
    dependencies=[Depends(require_roles("admin"))],
)
def list_requests(db: DbSession) -> list[RoleRequestDetail]:
    return [_to_detail(request) for request in role_request_service.list_role_requests(db)]


@router.post(
    "/{request_id}/approve",
    response_model=RoleRequestDetail,
)
def approve_request(
    request_id: uuid.UUID,
    db: DbSession,
    admin: Annotated[AuthenticatedUser, Depends(require_roles("admin"))],
) -> RoleRequestDetail:
    request = role_request_service.decide_role_request(db, request_id, True, uuid.UUID(admin.sub))
    return _to_detail(request)


@router.post(
    "/{request_id}/decline",
    response_model=RoleRequestDetail,
)
def decline_request(
    request_id: uuid.UUID,
    db: DbSession,
    admin: Annotated[AuthenticatedUser, Depends(require_roles("admin"))],
) -> RoleRequestDetail:
    request = role_request_service.decide_role_request(db, request_id, False, uuid.UUID(admin.sub))
    return _to_detail(request)
