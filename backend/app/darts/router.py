from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.darts.models import Game, GameCreate, GameRead, GameUpdate
from app.database import get_session


router = APIRouter(tags=["games"])


@router.get("/games/", response_model=List[GameRead])
async def get_games(*, session: Session = Depends(get_session)) -> List[GameRead]:
    """Get all games"""
    statement = select(Game)
    results = session.exec(statement)
    games = results.all()
    print(f"Games: {games}")
    return games


@router.post("/game/", response_model=GameRead)
async def create_game(post_game: GameCreate, session: Session = Depends(get_session)) -> GameRead:
    """Create a new game"""
    db_game = Game.model_validate(post_game)
    db_game.created_at = datetime.now()
    db_game.modified_at = datetime.now()
    session.add(db_game)
    session.commit()
    session.refresh(db_game)

    return db_game


@router.patch("/game/{game_id}", response_model=GameRead)
async def update_game(game_id: int, game: GameUpdate, session: Session = Depends(get_session)) -> GameRead:
    """Update an existing game"""
    db_game = session.get(Game, game_id)

    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")

    game_data = game.model_dump(exclude_unset=True)
    db_game.sqlmodel_update(game_data)
    db_game.modified_at = datetime.now()

    session.add(db_game)
    session.commit()
    session.refresh(db_game)

    return db_game
