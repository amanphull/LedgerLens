from fastapi import FastAPI

from backend.api.router import api_router
from backend.config.settings import settings
from backend.database.connection import Base, engine

# Import all models BEFORE create_all()
from backend.models.upload_model import Upload

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(api_router)


@app.get("/", tags=["Home"])
def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
    
    