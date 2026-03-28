import datetime
from pydantic import BaseModel, EmailStr

class UserRead(BaseModel):
    id: int
    email: EmailStr
    password_hash: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    disabled: bool
    is_verified: bool

class UserCreateRaw(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password_hash: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class ResetPasswordRequest(BaseModel):
    email: str
    password: str
    new_password: str
    
class ForgotPasswordRequest(BaseModel):
    email: str

    
class ForgotPasswordResetRequest(BaseModel):
    token: str
    password: str
    
class UserPasswordUpdate(BaseModel):
    message: str
    user_id: int
