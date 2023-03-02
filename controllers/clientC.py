from db import models, schemas
from sqlalchemy.orm import Session


def create_client(db: Session, client: schemas.ClientDetails):
    new_client = models.Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client


def read_client(db: Session, id: int):
    return db.query(models.Client).filter(models.Client.id == id).first()


def read_all_clients(db: Session, skip: int, limit: int):
    return db.query(models.Client).offset(skip).limit(limit).all()


def update_client(db: Session):
    ...

def delete_client(db:Session):
    ...

def deactivate_client(*, db:Session, id:int):
    ...

def reactivate_client(*, db:Session, id:int):
    ...