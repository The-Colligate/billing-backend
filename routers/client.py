from fastapi import APIRouter, Depends
from controllers import clientC as cc
from sqlalchemy.orm import Session
from db.database import get_db
from db import schemas

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/create")
def create_client(*, db: Session = Depends(get_db), client: schemas.ClientCreate):
    return cc.create_clients(db, client)


@router.get("/all")
def read_all_clients(*, db: Session = Depends(get_db), skip: int = 0, limit: int = 0):
    return cc.read_all_clients(db, skip, limit)


@router.get("/{id}")
def read_client(*, db: Session = Depends(get_db), id: int):
    return cc.read_client(db, id)
