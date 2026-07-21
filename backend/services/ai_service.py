from pathlib import Path

from sqlalchemy.orm import Session

from backend.ai.extractor import extract_invoice
from backend.models.upload_model import Upload


def process_invoice(
    upload_id: str,
    db: Session,
):

    upload = (
        db.query(Upload)
        .filter(Upload.id == upload_id)
        .first()
    )

    if upload is None:
        raise ValueError("Upload not found")

    image_path = Path("uploads") / upload.stored_filename

    result = extract_invoice(image_path)

    upload.vendor_name = result.get("vendor_name", "")
    upload.invoice_number = result.get("invoice_number", "")
    upload.invoice_date = result.get("invoice_date", "")
    upload.gst_number = result.get("gst_number", "")
    upload.total_amount = result.get("total_amount", 0)
    upload.tax_amount = result.get("tax_amount", 0)

    upload.ai_status = "Completed"
    upload.ai_confidence = result.get("confidence", 0)

    db.commit()
    db.refresh(upload)

    return {
        "message": "Invoice processed successfully",
        "data": result,
    }