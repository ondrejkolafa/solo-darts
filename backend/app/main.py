from contextlib import asynccontextmanager
from fastapi import FastAPI

# from app.darts import models
from app.database import create_db_and_tables
from app.routes import api_router

# models.Base.metadata.drop_all(bind=engine)
# models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(api_router)
