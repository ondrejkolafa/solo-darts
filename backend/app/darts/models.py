from app.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, text


class DbGame(Base):
    __tablename__ = "Game"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    game_type = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    rounds = Column(Integer, default=15)
    game_data = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    modified_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
