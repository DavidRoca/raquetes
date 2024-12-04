from fastapi import FastAPI
from backend.routers import auth
from backend.database import engine, Base
from starlette.middleware.sessions import SessionMiddleware

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="!secret")

# Include Routers
app.include_router(auth.router)
# app.include_router(player, prefix="/players", tags=["Players"])
# app.include_router(admin, prefix="/admins", tags=["Admins"])