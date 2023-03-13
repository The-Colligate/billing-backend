from sqlalchemy.orm import Session
from db import schemas, models
from fastapi import HTTPException, status
import json


def create_invoice(
    db: Session,
    invoice_info: schemas.InvoiceCreate,
    services: list[schemas.ServiceInvoice],
    client_id: int,
):
    # convert service objects to dict, or they will be stored as object instantiation strings
    parsed_services = str([s.dict() for s in services])
    new_invoice = models.Invoice(
        **invoice_info.dict(), client_id=client_id, services=parsed_services
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice.invoice_id


def generate_pdf(db: Session, invoice_id):
    """read an invoice,
    parse the services
    add a column for the cost of each service
    calculate the total cost
    add to HTML
    generate pdf
    """
    invoice = (
        db.query(models.Invoice).filter(models.Invoice.invoice_id == invoice_id).first()
    )

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found"
        )

    invoice.services = json.loads(invoice.services.replace("'", '"'))

    # return {json.loads(i) for i in json.loads(invoice.services)}
    return invoice
