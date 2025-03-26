from enum import Enum
from pydantic import BaseModel


class GameType(str, Enum):
    g_501 = "501"
    g_cricket = "cricket"

class GameStatus(int, Enum):
    in_progress = 0
    finished = 1


class Game(BaseModel):
    game_type: GameType
    status: GameStatus = GameStatus.in_progress
    description: str | None = None
    rounds:int = 15
