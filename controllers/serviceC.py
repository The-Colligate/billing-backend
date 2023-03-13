from sqlalchemy.orm import Session
from db import models

def read_services(db:Session):
    return db.query(models.Service).all()

def edit_service(db:Session)