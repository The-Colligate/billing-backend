from db import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError


def create_client(db: Session, client: schemas.ClientDetails):
    new_client = models.Client(**client.dict(), active=True)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client


def read_client(db: Session, id: int):
    client = db.query(models.Client).filter(models.Client.id == id).first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

    return client


def read_all_clients(db: Session, skip: int, limit: int):
    return db.query(models.Client).offset(skip).limit(limit).all()


def update_client(db: Session):
    client = db.query(models.Client).filter(models.Client.id == id).first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )


def update_client_tier(db: Session, client_id: int, new_tier: int):
    ...


def delete_client(db: Session, id):
    client = db.query(models.Client).filter(models.Client.id == id)

    if not client.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

    client.delete(synchronize_session=False)

    db.commit()


def deactivate_client(db: Session, id: int):
    client = db.query(models.Client).filter(models.Client.id == id)

    if not client.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

    client.update({"active": False})
    db.commit()

    return "updated"


def reactivate_client(db: Session, id: int):
    client = db.query(models.Client).filter(models.Client.id == id)

    if not client.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

    client.update({"active": True})
    db.commit()

    return "updated"


def create_focal_point(
    db: Session, focal_point: schemas.FocalPointBase, client_id: int
):
    # make sure the client exists
    client = db.query(models.Client).filter(models.Client.id == client_id)

    if not client.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

    # create focal point
    new_fp = models.FocalPoint(**focal_point.dict(), client_id=client_id)

    try:
        db.add(new_fp)
        db.commit()
        db.refresh(new_fp)

        # update client's focal point details
        client.update({"focal_point_id": new_fp.id})
        db.commit()

        return "updated"
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Client already has a focal point",
        )


def update_focal_point(db, client_id):
    ...


def remove_focal_point(db, client_id):
    client = db.query(models.Client).filter(models.Client.id == client_id)

    if not client.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
        )

    client.update({"focal_point_id": None})
    db.commit()

    return "updated"
