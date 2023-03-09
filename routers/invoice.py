from fastapi import APIRouter, Depends, Body
from db.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime
from controllers import invoiceC as ic


router = APIRouter(prefix="/invoice/")


@router.post("create_invoice/")
def create_invoice(
    *,
    db: Session = Depends(get_db),
    due_date: datetime,
    billing_start: datetime = Body(
        description="The date the current billing period began"
    ),
    billing_end: datetime = Body(
        description="The date the current billing period began"
    ),
    client_id: int
):
    return ic.create_invoice()
