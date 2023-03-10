from sqlalchemy.orm import Session
from db import models
from sqlalchemy.sql import func
from sqlalchemy import distinct


def count_clients(db: Session, plan: str):
    if plan.value == "all":
        return db.query(models.Client).count()
    elif plan.value == "voice":
        return db.query(func.count(distinct(models.Voice.client_id))).scalar()
    elif plan.value == "data":
        return db.query(func.count(distinct(models.Data.client_id))).scalar()


def count_invoices(db: Session, plan: str):
    if plan.value == "all":
        return db.query(models.Data).count() + db.query(models.Voice).count()
    elif plan.value == "voice":
        return db.query(models.Voice).count()
    elif plan.value == "data":
        return db.query(models.Data).count()


def calc_revenue(db: Session, plan: str):
    if plan.value == "all":
        return (
            db.query(func.sum(models.Voice.last_payment)).scalar()
            + db.query(func.sum(models.Data.last_payment)).scalar()
        )
    elif plan.value == "voice":
        return db.query(func.sum(models.Voice.last_payment)).scalar()
    elif plan.value == "data":
        return db.query(func.sum(models.Data.last_payment)).scalar()
 

def calc_loyalty(db: Session, plan: str):
    if plan.value == "all":
        ...
    elif plan.value == "voice":
        ...
    elif plan.value == "data":
        ...


def recent_invoices(db: Session, plan: str, len: int):
    if plan.value == "voice":
        return db.query(models.Voice).limit(len).all()
    elif plan.value == "data":
        return db.query(models.Data).limit(len).all()


def get_debt(db: Session, plan: str):
    if plan.value == "all":
        return (
            db.query(func.sum(models.Data.debit)).scalar()
            + db.query(func.sum(models.Voice.outstanding_debt)).scalar()
        )
    elif plan.value == "voice":
        return db.query(func.sum(models.Data.debit)).scalar()
    elif plan.value == "data":
        return db.query(func.sum(models.Voice.outstanding_debt)).scalar()
