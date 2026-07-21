from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models.upload_model import Upload


def approve_invoice(
    upload_id: str,
    db: Session,
):
    """
    Approve an invoice after manual review.
    """

    upload = (
        db.query(Upload)
        .filter(Upload.id == upload_id)
        .first()
    )

    if upload is None:
        raise HTTPException(
            status_code=404,
            detail="Upload not found",
        )

    upload.review_status = "Approved"
    upload.reviewed_at = datetime.utcnow()

    db.commit()
    db.refresh(upload)

    return {
        "success": True,
        "message": "Invoice approved successfully.",
        "data": {
            "id": upload.id,
            "review_status": upload.review_status,
            "reviewed_at": upload.reviewed_at,
        },
    }


def reject_invoice(
    upload_id: str,
    db: Session,
):
    """
    Reject an invoice after manual review.
    """

    upload = (
        db.query(Upload)
        .filter(Upload.id == upload_id)
        .first()
    )

    if upload is None:
        raise HTTPException(
            status_code=404,
            detail="Upload not found",
        )

    upload.review_status = "Rejected"
    upload.reviewed_at = datetime.utcnow()

    db.commit()
    db.refresh(upload)

    return {
        "success": True,
        "message": "Invoice rejected successfully.",
        "data": {
            "id": upload.id,
            "review_status": upload.review_status,
            "reviewed_at": upload.reviewed_at,
        },
    }