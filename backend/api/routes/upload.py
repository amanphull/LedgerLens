from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from typing import List

from backend.database.session import get_db
from backend.schemas.upload_schema import UploadResponse
from backend.services.upload_service import save_uploaded_file
from backend.schemas.upload_list_schema import UploadListResponse
from backend.services.upload_service import get_all_uploads
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
@router.get(
    "/uploads",
    response_model=List[UploadListResponse],
)
def list_uploads(
    db: Session = Depends(get_db),
):
    return get_all_uploads(db)