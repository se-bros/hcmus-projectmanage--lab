from typing import Literal

from pydantic import BaseModel, Field

Role = Literal["reader", "editor", "admin"]


class DevTokenRequest(BaseModel):
    role: Role = "reader"


class DevTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: Role


class RegisterRequest(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=72)


class LoginRequest(BaseModel):
    email: str
    password: str
