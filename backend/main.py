from fastapi import FastAPI

from backend.api.router import api_router
from backend.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Register all API routes
app.include_router(api_router)


@app.get("/", tags=["Home"])
def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }