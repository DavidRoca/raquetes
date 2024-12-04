from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database file located in the project root
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/app.db"  # SQLite file

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal will be used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print(f"Database file: {SQLALCHEMY_DATABASE_URL}")

# Base class for model definitions
Base = declarative_base()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()