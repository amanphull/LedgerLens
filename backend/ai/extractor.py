import json
import mimetypes
from pathlib import Path

from google import genai
from google.genai import types
from google.genai.errors import ClientError, ServerError

from backend.ai.prompts import INVOICE_EXTRACTION_PROMPT
from backend.config.settings import settings


# Initialize Gemini Client
client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
)


def extract_invoice(image_path: Path) -> dict:
    """
    Extract invoice information from an image using Gemini Vision.

    Returns:
        dict: Extracted invoice fields.

    Raises:
        RuntimeError: If Gemini API fails.
        ValueError: If Gemini returns invalid JSON.
    """

    mime_type = (
        mimetypes.guess_type(str(image_path))[0]
        or "image/jpeg"
    )

    with open(image_path, "rb") as file:
        image_bytes = file.read()

    try:

        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=[
                INVOICE_EXTRACTION_PROMPT,
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type=mime_type,
                ),
            ],
        )

    except ClientError as e:
        raise RuntimeError(
            f"Gemini Client Error: {e}"
        )

    except ServerError as e:
        raise RuntimeError(
            f"Gemini Server Error: {e}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Unexpected Gemini Error: {e}"
        )

    print("\n================ GEMINI RESPONSE ================\n")
    print(response.text)
    print("\n=================================================\n")

    if not response.text:
        raise ValueError(
            "Gemini returned an empty response."
        )

    cleaned_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(cleaned_text)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"""
Gemini returned invalid JSON.

Raw Response:

{response.text}

JSON Error:
{e}
"""
        )