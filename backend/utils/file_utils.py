from pathlib import Path
import uuid

from fastapi import HTTPException

from backend.core.constants import (
    ALLOWED_CONTENT_TYPES,
    MAX_UPLOAD_SIZE_BYTES,
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def generate_unique_filename(filename: str) -> str:
    extension = Path(filename).suffix
    return f"{uuid.uuid4()}{extension}"


def validate_content_type(content_type: str):

    if content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG images are allowed.",
        )


def validate_file_size(size: int):

    if size > MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=400,
            detail="File exceeds maximum upload size of 10 MB.",
        )