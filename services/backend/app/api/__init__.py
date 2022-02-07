from app.api import ping
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(ping.router, tags=["Ping"], prefix="/ping")
