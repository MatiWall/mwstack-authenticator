from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.db.setup import get_session
from app.services.security import get_password_hash, verify_password, create_access_token
from app.models.user import UserCreateRaw, UserCreate, Token, UserRead

from app.services.user import delete_user_by_id, get_all_users, get_user_by_email, register_user

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


from pydantic import BaseModel
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


# @router.get("/login", response_class=HTMLResponse)
# async def login_page(request: Request, redirect_uri: str):
#     return templates.TemplateResponse("login.html", {"request": request, "redirect_uri": redirect_uri})


# @router.post("/login")
# async def login_and_redirect(
#     username: str = Form(...),
#     password: str = Form(...),
#     redirect_uri: str = Form(...)
# ):
#     user = get_user_by_email(username)
#     if not user or not verify_password(password, user.password_hash):
#         # Optionally: re-render form with error message
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     access_token = create_access_token(data={"sub": str(user.id)})
#     redirect_url = f"{redirect_uri}?token={access_token}"

#     return RedirectResponse(url=redirect_url, status_code=302)
