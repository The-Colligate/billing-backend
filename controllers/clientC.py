from db import models, schemas
from sqlalchemy.orm import Session


def create_client(db: Session, client: schemas.ClientCreate):
    new_customer = models.Client(client)
    db.add(new_customer)
    db.commit()
    db.refresh()


def read_client(db: Session, id: int):
    return db.query(models.Client).filter(models.Client.id == id).first()


def read_all_clients(db: Session, skip: int, limit: int):
    return db.query(models.Client).offset(skip).limit(limit)


def update_client(db: Session):
    ...
