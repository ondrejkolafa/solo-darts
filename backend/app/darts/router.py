from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.darts.schemas import Game, GameCreate
from app.darts import models
from app.database import get_db


router = APIRouter(prefix="/games", tags=["games"])


@router.get("/games/", response_model=List[Game])
async def get_games(db: Session = Depends(get_db)):
    games = db.query(models.DbGame).all()
    return games


@router.post("/game/")
async def create_game(post_game: GameCreate, db: Session = Depends(get_db)) -> List[Game]:

    new_game = models.DbGame(**post_game.model_dump())
    new_game.created_at = datetime.now()
    new_game.modified_at = datetime.now()
    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return [new_game]


@router.patch("/game/")
async def update_game(
    game_id: int, expected: list[int], throws: list[int], db: Session = Depends(get_db)
) -> List[Game]:

    if not game_id:
        return {"error": "game_id is required"}
    if not expected:
        return {"error": "expected list is required"}
    if not throws:
        return {"error": "throws list is required"}

    print(f"game_id: {game_id}, expected: {expected}, throws: {throws}")

    game = db.query(models.DbGame).filter(models.DbGame.id == game_id).first()
    if throws and expected and game:
        if game.game_data:
            print(f"Modifying existing game data: {game.game_data}")
            game.game_data["round"] += 1
            game.game_data["expected"] = expected
            game.game_data["throws"] = throws
        else:
            game.game_data = {"round": 1, "expected": expected, "throws": throws}
            print(f"Creating new game data: {game.game_data}")
    game.modified_at = datetime.now()

    print(f"game: {game.__dict__}")

    db.add(game)
    db.commit()
    db.refresh(game)

    return [game]
