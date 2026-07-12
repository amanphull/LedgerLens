from pathlib import Path
import shutil

from fastapi import HTTPException, UploadFile

from backend.utils.file_utils import (
    UPLOAD_DIR,
    generate_unique_filename,
)


async def save_uploaded_file(file: UploadFile):

    allowed_types = [
        "image/jpeg",
        "image/png",
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG images are allowed.",
        )

    filename = generate_unique_filename(file.filename)

    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Upload Successful",
        "original_filename": file.filename,
        "stored_filename": filename,
        "content_type": file.content_type,
    }