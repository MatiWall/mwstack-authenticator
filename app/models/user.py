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
    
