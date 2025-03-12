from app.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class DbGame(Base):
    __tablename__ = "Game"

    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    description = Column(String,nullable=True)
    rounds = Column(Integer, default=15)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))