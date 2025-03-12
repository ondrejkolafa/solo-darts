from fastapi import FastAPI

from app.darts import models
from app.database import engine
from app.routes import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hi")
async def root():
    return {"message": "Hi"}


app.include_router(api_router)