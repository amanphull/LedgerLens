from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.review_service import (
    approve_invoice,
    reject_invoice,
)

router = APIRouter()


@router.post("/review/{upload_id}/approve")
def approve(
    upload_id: str,
    db: Session = Depends(get_db),
):
    return approve_invoice(upload_id, db)


@router.post("/review/{upload_id}/reject")
def reject(
    upload_id: str,
    db: Session = Depends(get_db),
):
    return reject_invoice(upload_id, db)