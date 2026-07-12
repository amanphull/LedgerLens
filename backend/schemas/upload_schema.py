from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    original_filename: str
    stored_filename: str
    content_type: str