from sqlalchemy.orm import Session
from datetime import datetime


def create_invoice(db: Session, billing_start: datetime):
    date_created = datetime.now()
    # billing_period =
