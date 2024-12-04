from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tennis_app.database import get_db
#from tennis_app.models.player import Player
from tennis_app.auth.jwt import get_current_user

router = APIRouter(prefix="/players", tags=["Players"])

# @router.get("/", response_model=list)
# def get_players(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
#     # The user is authenticated if this point is reached
#     return db.query(Player).all()

