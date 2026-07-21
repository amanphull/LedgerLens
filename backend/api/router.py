from fastapi import APIRouter

from backend.api.routes.ai import router as ai_router
from backend.api.routes.review import router as review_router
from backend.api.routes.upload import router as upload_router

api_router = APIRouter()

api_router.include_router(upload_router)
api_router.include_router(ai_router)
api_router.include_router(review_router)