from fastapi import APIRouter

from backend.ai.client import client
from backend.config.settings import settings

router = APIRouter()


@router.get("/test-openai")
def test_openai():

    response = client.responses.create(
        model=settings.OPENAI_MODEL,
        input="Reply with exactly these two words: OpenAI Connected"
    )

    return {
        "response": response.output_text
    }