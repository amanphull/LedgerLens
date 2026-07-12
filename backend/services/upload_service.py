from fastapi import UploadFile
from sqlalchemy.orm import Session
from pathlib import Path
import shutil
from backend.models.upload_model import Upload
from backend.utils.file_utils import (
    UPLOAD_DIR,
    generate_unique_filename,
    validate_content_type,
    validate_file_size,
)


async def save_uploaded_file(
    file: UploadFile,
    db: Session,
):


    validate_content_type(file.content_type)

    content = await file.read()

    validate_file_size(len(content))

    file.file.seek(0)

    filename = generate_unique_filename(file.filename)

    file_path = UPLOAD_DIR / filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    upload = Upload(
        original_filename=file.filename,
        stored_filename=filename,
        content_type=file.content_type,
    )

    db.add(upload)
    db.commit()
    db.refresh(upload)

    return {
        "message": "Upload Successful",
        "id": upload.id,
        "original_filename": upload.original_filename,
        "stored_filename": upload.stored_filename,
        "content_type": upload.content_type,
        "status": upload.status,
    }
def get_all_uploads(db):
    return (
        db.query(Upload)
        .order_by(Upload.upload_time.desc())
        .all()
    )