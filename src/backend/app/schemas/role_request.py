from datetime import datetime
from typing import Literal

from pydantic import BaseModel

RequestStatus = Literal["pending", "approved", "rejected"]


class RoleRequestDetail(BaseModel):
    id: str
    user_id: str
    user_email: str
    user_username: str | None
    requested_role: str
    status: RequestStatus
    created_at: datetime
    decided_at: datetime | None
