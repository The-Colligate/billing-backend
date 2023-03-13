from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from controllers import invoiceC as ic
from db import schemas


router = APIRouter(prefix="/invoice", tags=["invoice"])


@router.post("/create_invoice/")
def create_invoice(
    *,
    db: Session = Depends(get_db),
    invoice_info: schemas.InvoiceCreate,
    services: list[schemas.ServiceInvoice],
    client_id: int
):
    """Send in details for creating an invoice. A PDF is generated and sent to the focal point"""
    invoice_id = ic.create_invoice(db, invoice_info, services, client_id)
    return ic.generate_pdf(db, invoice_id)


