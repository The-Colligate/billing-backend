from fastapi import APIRouter, Depends
from controllers import clientC as cc
from sqlalchemy.orm import Session
from db.database import get_db
from db import schemas

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/create", response_model=schemas.ClientID)
def create_client(*, db: Session = Depends(get_db), client: schemas.ClientDetails):
    return cc.create_client(db, client)


@router.get("/all", response_model=list[schemas.ClientID])
def read_all_clients(*, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return cc.read_all_clients(db, skip, limit)


@router.get("/{id}")
def read_client(*, db: Session = Depends(get_db), id: int):
    return cc.read_client(db, id)

@router.put('/{id}')
def update_client(*, db:Session = Depends(get_db), id:int):
    return cc.update_client(db, id)

@router.delete

@router.post('/deactivate')
def deactivate_client(*, db:Session = Depends(get_db), id:int):
    return cc.deactivate_client(db, id)

@router.post('/reactivate')
def reactivate_client(*, db:Session = Depends(get_db), id:int):
    return cc.reactivate_client(db, id)
