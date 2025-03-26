from app.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, text


class DbGame(Base):
    __tablename__ = "Game"

    id = Column(Integer,primary_key=True,nullable=False)
    game_type = Column(String,nullable=False)
    status = Column(Integer,nullable=False)
    description = Column(String,nullable=True)
    rounds = Column(Integer, default=15)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))