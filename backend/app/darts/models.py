from datetime import datetime
from enum import Enum
from sqlmodel import Column, Field, JSON, SQLModel


class GameType(str, Enum):
    G_501 = "501"
    G_CRICKET = "cricket"


class GameStatus(int, Enum):
    IN_PROGRESS = 0
    FINISHED = 1


class Throws(SQLModel):
    throws: list[str] = Field(
        default=[],
        sa_column=Column(JSON),
        schema_extra={"example": ["D20", "T1", "5"]},
    )
    expected: list[str] = Field(
        default=[],
        sa_column=Column(JSON),
        schema_extra={"example": ["20", "20", "20"]},
    )


class GamesBase(SQLModel):
    game_type: GameType = Field(default=GameType.G_501, sa_column_kwargs={"nullable": False})
    status: GameStatus = Field(default=GameStatus.IN_PROGRESS, sa_column_kwargs={"nullable": False})
    description: str | None = Field(default=None, sa_column_kwargs={"nullable": True})
    rounds: int = Field(default=15, sa_column_kwargs={"nullable": False})
    throws: list[Throws] = Field(default=[], sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"nullable": False})
    modified_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"nullable": False})


class Game(GamesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class GameRead(GamesBase):
    id: int


class GameCreate(GamesBase):
    pass


# class GameThrows(SQLModel):
#     throws: Throws = Field(
#         default=[],
#         sa_column=Column(JSON),
#         schema_extra={"example": {"throws": ["D20", "T1", "5"], "expected": ["20", "20", "20"]}},
#     )
