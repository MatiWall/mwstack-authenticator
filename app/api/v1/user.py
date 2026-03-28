import logging
logger = logging.getLogger(__name__)

from pydantic import BaseModel
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.db.setup import get_session
from app.services.security import decode_reset_password_token, get_password_hash, verify_password, create_access_token
from app.models.user import ForgotPasswordRequest, ForgotPasswordResetRequest, UserCreateRaw, UserCreate, Token, UserRead, ResetPasswordRequest

from app.services.user import (
    delete_user_by_id,
    forgot_user_password_reset, 
    get_all_users, 
    get_user_by_email, 
    register_user, 
    reset_user_password,
    send_reset_email
)

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register", response_model=UserRead)
async def post_user(
    user: UserCreateRaw,
    session: Session = Depends(get_session)
    ):
    user_data = UserCreate(
        email=user.email,
        password_hash=get_password_hash(user.password)
    )
    return register_user(user_data, session)

@router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: int):
    
    try:
        delete_success = delete_user_by_id(user_id)
        if not delete_success:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/all", response_model=list[UserRead])
def read_users():
    """Fetch all users."""
    users = get_all_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users



class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/token", response_model=Token)
def login(form_data: LoginRequest, session: Session = Depends(get_session)):
    user = get_user_by_email(form_data.username, session)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/forgot-password")
def forgot_password(reset_request: ForgotPasswordRequest, session: Session = Depends(get_session)):
    
    user = get_user_by_email(reset_request.email, session)

    if user:
        send_reset_email(reset_request.email)
        
    if not user:
        logger.warning(f"Password reset requested for non-existent email: {reset_request.email}")


    return {"message": f"If a user with email {reset_request.email} exists, a password reset link has been sent."}

@router.post("/forgot-password-reset")
def forgot_password_reset(reset_request: ForgotPasswordResetRequest, session: Session = Depends(get_session)):
    return forgot_user_password_reset(reset_request, session)
    


@router.post("/reset-password")
def reset_password(
    reset_request: ResetPasswordRequest, 
    session: Session = Depends(get_session)
    ):
    return reset_user_password(reset_request, session)