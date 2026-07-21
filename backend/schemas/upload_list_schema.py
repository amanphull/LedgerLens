from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UploadListResponse(BaseModel):
    id: str

    original_filename: str

    stored_filename: str

    content_type: str

    upload_time: datetime

    status: str

    vendor_name: Optional[str] = None

    invoice_number: Optional[str] = None

    invoice_date: Optional[str] = None

    gst_number: Optional[str] = None

    total_amount: Optional[float] = None

    tax_amount: Optional[float] = None

    ai_status: Optional[str] = None

    ai_confidence: Optional[float] = None

    review_status: Optional[str] = None

    reviewed_at: Optional[datetime] = None

    class Config:
        from_attributes = True