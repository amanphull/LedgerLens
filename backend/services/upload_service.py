from pathlib import Path
import shutil

from fastapi import UploadFile

from backend.utils.file_utils import (
    UPLOAD_DIR,
    generate_unique_filename,
    validate_content_type,
    validate_file_size,
)


async def save_uploaded_file(file: UploadFile):

    validate_content_type(file.content_type)

    content = await file.read()

    validate_file_size(len(content))

    file.file.seek(0)

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
    