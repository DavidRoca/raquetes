from passlib.context import CryptContext
from sqlalchemy.orm import Session

import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tennis_app.database import SessionLocal

from tennis_app.models.user import User

# Set up password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Example users with hashed passwords
example_users = [
    {"email": "user1@example.com", "password": "password123", "role": "player", "is_active": True},
    {"email": "admin@example.com", "password": "admin123", "role": "admin", "is_active": True},
    {"email": "inactiveuser@example.com", "password": "password456", "role": "player", "is_active": False},
]

def seed_users(db: Session):
    """
    Add example users to the users table.
    """
    for user_data in example_users:
        user_data["password"] = hash_password(user_data["password"])  # Hash password before saving
        user = User(**user_data)
        db.add(user)
    db.commit()

def main():
    db = SessionLocal()
    seed_users(db)
    print("Example users added to the database.")

if __name__ == "__main__":
    main()
