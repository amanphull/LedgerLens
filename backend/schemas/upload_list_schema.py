from datetime import datetime

from pydantic import BaseModel


class UploadListResponse(BaseModel):
    id: str
    original_filename: str
    stored_filename: str
    content_type: str
    upload_time: datetime
    status: str

    class Config:
        from_attributes = True