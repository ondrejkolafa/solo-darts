from pydantic import BaseModel

class Game(BaseModel):
    name: str
    description: str | None = None
    rounds:int = 15