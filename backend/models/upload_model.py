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

    original_filename = Column(String, nullable=False)

    stored_filename = Column(String, nullable=False)

    content_type = Column(String, nullable=False)

    upload_time = Column(
        DateTime,
        default=datetime.utcnow,
    )

    status = Column(
        String,
        default="Uploaded",
    )

    ai_confidence = Column(
        Float,
        nullable=True,
    )