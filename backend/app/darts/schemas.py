from enum import Enum
from pydantic import BaseModel


class GameType(str, Enum):
    G_501 = "501"
    G_CRICKET = "cricket"


class GameStatus(int, Enum):
    IN_PROGRESS = 0
    FINISHED = 1


class Game(BaseModel):
    game_type: GameType
    status: GameStatus = GameStatus.IN_PROGRESS
    description: str | None = None
    rounds:int = 15
    game_data:dict = {}
