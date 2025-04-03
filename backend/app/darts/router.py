import copy
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.darts.models import Game, GameCreate, GameRead, Throws
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
async def throw_darts(game_id: int, throws: Throws, session: Session = Depends(get_session)) -> GameRead:
    """Update an existing game"""
    db_game = session.get(Game, game_id)

    print(f"Game: {db_game}")
    print(f"Throws: {throws}")

    if not db_game:
        raise HTTPException(status_code=404, detail="Game not found")

    # db_throws = db_game.throws or []
    db_throws = copy.deepcopy(db_game.throws) if db_game.throws else []
    db_throws.append(throws.model_dump())

    db_game.throws = list(db_throws)  # Explicitly assign a new list to ensure changes are tracked
    db_game.modified_at = datetime.now()

    session.add(db_game)  # Ensure the session is aware of the changes
    print(f"Game updated: {db_game}")

    session.add(db_game)
    session.commit()
    session.refresh(db_game)

    return db_game
