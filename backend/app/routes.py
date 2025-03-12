from fastapi import APIRouter

from app.darts import router as router_darts

api_router = APIRouter()

api_router.include_router(router_darts.router)