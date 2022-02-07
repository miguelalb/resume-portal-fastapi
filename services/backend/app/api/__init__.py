from app.api import ping, profile, user
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(ping.router, tags=["Ping"], prefix="/ping")
api_router.include_router(user.router, tags=["User"], prefix="/users")
api_router.include_router(ping.router, tags=["Profile"], prefix="/profile")
