from typing import Literal

from pydantic import BaseModel

Role = Literal["reader", "editor", "admin"]


class DevTokenRequest(BaseModel):
    role: Role = "reader"


class DevTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: Role
