import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    password_hash: str
    verification_token: Optional[str] = None
    reset_password_token: Optional[str] = None
    is_verified: bool = False
    disabled: bool = False
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
    updated_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))


class Session(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    user_id: int = Field(foreign_key='user.id')
    refresh_token: str
    expires_at: datetime.datetime
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))

# class AuditLog(SQLModel, table=True):
#     id: Optional[int] = Field(primary_key=True, default=None)
#     user_id: int
#     action: str  # e.g., "login", "password_reset"
#     ip_address: Optional[str] = None
#     user_agent: Optional[str] = None
#     created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))


# class Role(SQLModel, table=True):
#     id: Optional[int] = Field(primary_key=True, default=None)
#     name: str
#     description: Optional[str] = None

# class UserRole(SQLModel, table=True):
#     user_id: int
#     role_id: int
