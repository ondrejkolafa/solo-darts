from datetime import datetime
from enum import Enum
from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class GameType(str, Enum):
    G_501 = "501"
    G_CRICKET = "cricket"


class GameStatus(int, Enum):
    IN_PROGRESS = 0
    FINISHED = 1


class GamesBase(SQLModel):
    game_type: GameType = Field(default=GameType.G_501, sa_column_kwargs={"nullable": False})
    status: GameStatus = Field(default=GameStatus.IN_PROGRESS, sa_column_kwargs={"nullable": False})
    description: str | None = Field(default=None, sa_column_kwargs={"nullable": True})
    rounds: int = Field(default=15, sa_column_kwargs={"nullable": False})
    game_data: dict = Field(default={"round": 0, "expected": [], "throws": []}, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"nullable": False})
    modified_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"nullable": False})


class Game(GamesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class GameRead(GamesBase):
    id: int


class GameCreate(GamesBase):
    pass


class GameUpdate(SQLModel):
    rounds: int | None
    game_data: dict | None
