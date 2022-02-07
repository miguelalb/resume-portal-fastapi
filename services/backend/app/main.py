from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.config import get_settings


def create_application() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.PROJECT_NAME)
    
    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin)
                           for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    app.include_router(api_router)

    return app


app = create_application()
