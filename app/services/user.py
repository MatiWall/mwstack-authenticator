import logging

from fastapi import HTTPException
from sqlmodel import Session, select

from app.models import user
from app.services.email import send_email
from app.services.security import create_reset_password_token, decode_reset_password_token, get_password_hash, verify_password
logger = logging.getLogger(__name__)
from app.db.models import User
from app.models.user import UserCreate, UserPasswordUpdate, UserRead
from app.settings import config

def register_user(user: UserCreate, session: Session) -> UserRead:
    logger.info(f"Registering user: {user.email}: {user}")
    if get_user_by_email(user.email, session):
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user_create = User(
        email=user.email,
        password_hash=user.password_hash
    )

    session.add(user_create)
    session.commit()
    session.refresh(user_create)

    logger.info(f"User registered successfully: {user.email}")
    return UserRead(
            id=user_create.id,
            email=user_create.email,
            password_hash=user.password_hash,
            created_at=user_create.created_at,
            updated_at=user_create.updated_at,
            is_verified=user_create.is_verified,
            disabled=user_create.disabled
        )
 

def get_all_users(session: Session) -> list[UserRead]:
    statement = select(User)
    results = session.exec(statement).all()

    return [
        UserRead(
            id=user.id,
            email=user.email,
            password_hash=user.password_hash,
            created_at=user.created_at,
            updated_at=user.updated_at,
            is_verified=user.is_verified,
            disabled=user.disabled
        )
        for user in results
    ]

    
def get_user_by_email(email: str, session: Session) -> UserRead:
    
    statement = select(User).where(User.email == email)
    
    result = session.exec(statement).one_or_none()
    
    if result:
        return UserRead(
            id=result.id,
            email=result.email,
            password_hash=result.password_hash,
            created_at=result.created_at,
            updated_at=result.updated_at,
            disabled=result.disabled, 
            is_verified=result.is_verified
        )
    return None

def delete_user_by_id(user_id: int, session: Session) -> UserRead:
    logger.info(f"Deleting user with ID: {user_id}")

    user = session.get(User, user_id)
    if not user:
        logger.warning(f"User not found: {user_id}")
        return False

    session.delete(user)
    session.commit()

    logger.info(f"User deleted successfully: {user_id}")
    return UserRead(
            id=user.id,
            email=user.email,
            password_hash=user.password_hash,
            created_at=user.created_at,
            updated_at=user.updated_at,
            disabled=user.disabled, 
            is_verified=user.is_verified
        )
    
def reset_user_password(reset_request: user.ResetPasswordRequest, session: Session):
    db_user = session.exec(select(User).filter(User.email == reset_request.email)).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(reset_request.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid current password")

    db_user.password_hash = get_password_hash(reset_request.new_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return UserPasswordUpdate(message="Password reset successful", user_id=db_user.id)


def send_reset_email(email: str):
    token = create_reset_password_token(email)
    url = f"{config.base_url}/{config.url_forgot_password}?token={token}"
    
    body = f"""
        <h2>Reset your password</h2>

        <p>We received a password reset request for your account associated with {email}.</p>

        <p>Click the button below to choose a new password:</p>

        <a href="{url}" 
        style="
            display:inline-block;
            padding:12px 20px;
            background:#000;
            color:#fff;
            text-decoration:none;
            border-radius:6px;
            font-weight:bold;
        ">
        Reset Password
        </a>

        <p>This link will expire in 30 minutes.</p>

        <p>If you did not request this, you can safely ignore this email.</p>

        <p>— MWStack Security</p>
    """
    
    send_email(
        to_email=email,
        subject="Password Reset Request",
        body=body
    )


    pass

def forgot_user_password_reset(reset_request: user.ForgotPasswordResetRequest, session: Session):  
    email = decode_reset_password_token(reset_request.token)  # This will raise an error if the token is invalid or expired
    db_user = session.exec(select(User).filter(User.email == email)).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.password_hash = get_password_hash(reset_request.password)
    session.add(db_user)
    session.commit()
    
    return {"success": True, "message": "Password reset successful"}