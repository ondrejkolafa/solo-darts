# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:adminpwd@db:5432/darts'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# print(f"Connecting to database: {engine} on {engine.url.host}:{engine.url.port}")

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlmodel import create_engine, Session, SQLModel

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:adminpwd@db:5432/darts"

connect_args = {}
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args=connect_args)


def create_db_and_tables():
    # SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
