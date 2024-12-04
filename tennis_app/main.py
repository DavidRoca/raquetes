from fastapi import FastAPI
from tennis_app.routers import auth
from tennis_app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include Routers
app.include_router(auth.router)
# app.include_router(player, prefix="/players", tags=["Players"])
# app.include_router(admin, prefix="/admins", tags=["Admins"])