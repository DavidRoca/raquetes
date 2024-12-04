from sqlalchemy import Column, Integer, String, Boolean
from tennis_app.database import Base

class User(Base):
    """
    SQLAlchemy User model for storing application users.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="player")  # Possible roles: "player", "admin"
    is_active = Column(Boolean, default=True)  # Indicates if the user is active

    # Allow redefining the table's options if it already exists
    __table_args__ = {'extend_existing': True}