from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from backend.database import get_db
from backend.models.user import User
from backend.schemas.user import UserCreate, UserLogin
from backend.auth.jwt import create_access_token
from backend.auth.password import verify_password
from fastapi import Request, Depends
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.responses import RedirectResponse
import os

router = APIRouter(prefix="/auth", tags=["Auth"])

# Configuration for OAuth
config = Config(environ=os.environ)
oauth = OAuth(config)

# Register OAuth clients (Google and Facebook)
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

facebook = oauth.register(
    name='facebook',
    client_id='YOUR_FACEBOOK_CLIENT_ID',
    client_secret='YOUR_FACEBOOK_CLIENT_SECRET',
    authorize_url='https://www.facebook.com/dialog/oauth',
    authorize_params=None,
    access_token_url='https://graph.facebook.com/v10.0/oauth/access_token',
    access_token_params=None,
    client_kwargs={'scope': 'email'},
)

@router.post("/register", response_model=dict)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already registered
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered",
        )

    # Hash the password and save the user
    hashed_password = bcrypt.hash(user.password)
    new_user = User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login", response_model=dict)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first() #TODO: Check this comparison
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    # Add role to token payload
    token = create_access_token({"sub": db_user.email, "role": db_user.role})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/login/{provider}")
async def login(request: Request, provider: str):
    if provider == "google":
        redirect_uri = request.url_for('auth')
        return await oauth.google.authorize_redirect(request, redirect_uri)
    elif provider == "facebook":
        redirect_uri = request.url_for('auth')
        return await oauth.facebook.authorize_redirect(request, redirect_uri)

@router.get('/auth')
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = token['userinfo']
    # Process user information here (e.g., create user in DB, create JWT, etc.)
    return RedirectResponse(url="/")