from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.darts.schemas import Game
from app.darts import models
from app.database import get_db


router = APIRouter(prefix="/games", tags=["games"])


@router.get("/games/", response_model=List[Game])
async def get_games(db: Session = Depends(get_db)):
    games = db.query(models.DbGame).all()
    return  games

@router.post("/game/")
async def create_game(post_game:Game, db:Session = Depends(get_db)):

    new_game = models.DbGame(**post_game.model_dump())
    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return [new_game]