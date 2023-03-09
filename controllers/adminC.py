from sqlalchemy.orm import Session
from db import schemas, models
from pydantic import EmailStr
from controllers.authC import hashp


def create_admin(db: Session, name: str, email: EmailStr, password: str):
    # by default, new admins are level 1
    new_admin = models.Admin(
        name=name, email=email, level=1, hashed_password=hashp(password)
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


def read_admin_by_email(db: Session, email: EmailStr):
    admin = db.query(models.Admin).filter(models.Admin.email == email).first()

    return admin
