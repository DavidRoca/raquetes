from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.jwt import get_current_user
from app.database import get_db
from app.models.user import User

def get_current_active_user(db: Session = Depends(get_db), token: str = Depends(get_current_user)):
    """
    Extract the currently logged-in user from the token and fetch user details from the database.
    """
    user_data = get_current_user(token)
    user = db.query(User).filter(User.email == user_data.sub).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user

def get_current_admin(db: Session = Depends(get_db), token: str = Depends(get_current_user)):
    """
    Ensure the current user is a club admin.
    """
    user = get_current_active_user(db, token)
    if user.role != "admin":  # Adjust for `is_club_admin` if using boolean
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: Admins only",
        )
    return user