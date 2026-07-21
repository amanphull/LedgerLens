from fastapi import APIRouter
from google import genai

from backend.config.settings import settings

router = APIRouter()


@router.get("/list-models")
def list_models():
    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    models = []

    for model in client.models.list():
        models.append(model.name)

    return {"models": models}