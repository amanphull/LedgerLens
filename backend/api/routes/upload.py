from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.schemas.upload_schema import UploadResponse
from backend.services.upload_service import save_uploaded_file

router = APIRouter()


@router.post(
    "/upload",
    response_model=UploadResponse,
)
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return await save_uploaded_file(file, db)