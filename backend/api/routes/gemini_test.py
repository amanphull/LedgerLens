from fastapi import APIRouter
from google import genai

from backend.config.settings import settings

router = APIRouter()


@router.get("/test-gemini")
def test_gemini():

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY,
    )

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents="Reply with exactly these two words: Gemini Connected",
    )

    return {
        "response": response.text
    }