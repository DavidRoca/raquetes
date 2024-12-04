from fastapi import APIRouter

#from tennis_app.models.player import Player

router = APIRouter(prefix="/players", tags=["Players"])

# @router.get("/", response_model=list)
# def get_players(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
#     # The user is authenticated if this point is reached
#     return db.query(Player).all()

