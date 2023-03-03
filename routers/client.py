from fastapi import APIRouter, Depends, status, Form
from controllers import clientC as cc
from sqlalchemy.orm import Session
from db.database import get_db
from db import schemas
from utils import Tier
from pydantic import EmailStr

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post(
    "/create", response_model=schemas.ClientID, status_code=status.HTTP_201_CREATED
)
def create_client(*, db: Session = Depends(get_db), client: schemas.ClientDetails):
    return cc.create_client(db, client)


@router.get("/all", response_model=list[schemas.ClientID])
def read_all_clients(*, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return cc.read_all_clients(db, skip, limit)


@router.get("/{id}", response_model=schemas.Client)
def read_client(*, db: Session = Depends(get_db), id: int):
    return cc.read_client(db, id)


@router.put("/update_tier/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_client_tier(
    *, db: Session = Depends(get_db), client_id: int, new_tier: Tier
):
    return cc.update_client_tier(db, client_id, new_tier)


@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_client(
    *,
    db: Session = Depends(get_db),
    id: int,
    name: str = Form(default=None),
    cac_id: str = Form(default=None),
    tin_id: str = Form(default=None),
    address: str = Form(default=None),
    website: str = Form(default=None),
    description: str = Form(default=None),
):
    """Update client details"""
    return cc.update_client(db, id, name, cac_id, tin_id, address, website, description)


@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_client(*, db: Session = Depends(get_db), id: int):
    return cc.delete_client(db, id)


@router.post("/deactivate", status_code=status.HTTP_202_ACCEPTED)
def deactivate_client(*, db: Session = Depends(get_db), id: int):
    return cc.deactivate_client(db, id)


@router.post("/reactivate", status_code=status.HTTP_202_ACCEPTED)
def reactivate_client(*, db: Session = Depends(get_db), id: int):
    return cc.reactivate_client(db, id)


@router.post("/{client_id}/set_focal_point", status_code=status.HTTP_201_CREATED)
def set_focal_point(
    *,
    db: Session = Depends(get_db),
    focal_point: schemas.FocalPoint,
    client_id: int,
):
    """create a focal point, then attach them to the client they represent"""
    return cc.create_focal_point(db, focal_point, client_id)


# @router.get("/{client_id}/focal-point")
# def read_focal_point(*, db: Session = Depends(get_db), client_id: int):
#     return cc.read_focal_point(db, client_id)


@router.put("/{client_id}/focal_point")
def update_focal_point(
    *,
    db: Session = Depends(get_db),
    name: str = Form(default=None),
    email: EmailStr = Form(default=None),
    phone: str = Form(default=None),
    client_id: int,
):
    return cc.update_focal_point(db, name, email, phone, client_id)


@router.delete("/{client_id}/focal_point")
def remove_focal_point(*, db: Session = Depends(get_db), client_id: int):
    return cc.remove_focal_point(db, client_id)
