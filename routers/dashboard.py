from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(tags=['dashboard'])

@router.get('/count_clients')
def count_clients(db:Session = Depends(get_db)):
    return {'message':'hey hey'}