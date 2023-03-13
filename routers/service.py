from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import schemas
from controllers import serviceC as sc

router = APIRouter(prefix='/services', tags='services')

@router.get('/all/')
def read_services(*,
    db: Session = Depends(get_db)):
    return sc.read_services(db)

@router.post('/new')
def create_service(*, db:Session = Depends(get_db), service:schemas.ServiceEdit):
    return sc.create_services(db, service)

@router.put('/{id}')
def update_rate(*, db:Session = Depends(get_db), service:schemas.ServiceEdit):
    return sc.edit_service(db, service)