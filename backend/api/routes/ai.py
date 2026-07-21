from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services.ai_service import process_invoice

router = APIRouter()


@router.post("/process/{upload_id}")
def process(upload_id: str, db: Session = Depends(get_db)):
    return process_invoice(upload_id, db)