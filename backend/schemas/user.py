from pydantic import EmailStr

from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserBase(BaseModel):
    email: str
    password: str
    role: Optional[str] = "player"  # Default to 'player'


class UserResponse(UserBase):
    """Schema for user response (response data)."""
    id: int
    is_active: bool

    class Config:
        orm_mode = True  # To allow conversion from ORM models (SQLAlchemy)