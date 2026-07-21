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


class UserProfile(BaseModel):
    id: str
    email: str | None
    username: str | None
    role: Role
    auth_provider: str
    has_password: bool


class UpdateProfileRequest(BaseModel):
    username: str | None = Field(default=None, max_length=255)


class ChangePasswordRequest(BaseModel):
    current_password: str | None = None
    new_password: str = Field(min_length=8, max_length=72)
