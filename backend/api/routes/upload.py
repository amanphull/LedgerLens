from fastapi import APIRouter, File, UploadFile

from backend.schemas.upload_schema import UploadResponse
from backend.services.upload_service import save_uploaded_file

router = APIRouter()


@router.post(
    "/upload",
    response_model=UploadResponse,
)
async def upload_file(
    file: UploadFile = File(...)
):
    return await save_uploaded_file(file)