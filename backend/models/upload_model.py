import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, String

from backend.database.connection import Base


class Upload(Base):
    __tablename__ = "uploads"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )

    # File Information
    original_filename = Column(
        String,
        nullable=False,
    )

    stored_filename = Column(
        String,
        nullable=False,
    )

    content_type = Column(
        String,
        nullable=False,
    )

    # AI Extracted Fields
    vendor_name = Column(
        String,
        nullable=True,
    )

    invoice_number = Column(
        String,
        nullable=True,
    )

    invoice_date = Column(
        String,
        nullable=True,
    )

    gst_number = Column(
        String,
        nullable=True,
    )

    total_amount = Column(
        Float,
        nullable=True,
    )

    tax_amount = Column(
        Float,
        nullable=True,
    )

    ai_status = Column(
        String,
        default="Pending",
    )

    ai_confidence = Column(
        Float,
        nullable=True,
    )

    # Upload Information
    upload_time = Column(
        DateTime,
        default=datetime.utcnow,
    )

    status = Column(
        String,
        default="Uploaded",
    )
    review_status = Column(
        String,
        default="Pending",
    )

    reviewed_at = Column(
        DateTime,
        nullable=True,
    )