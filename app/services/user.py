import logging

from fastapi import HTTPException
from sqlmodel import Session, select
logger = logging.getLogger(__name__)
from app.db.models import User
from app.models.user import UserCreate, UserRead

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