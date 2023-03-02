from fastapi import APIRouter, Depends, Form
from db.database import get_db
from sqlalchemy.orm import Session
from pydantic import EmailStr
from controllers import adminC as adc
from controllers import authC as ac
from db import schemas

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/signup", response_model=schemas.Admin)
def signup(
    *,
    db: Session = Depends(get_db),
    name: str = Form(),
    email: EmailStr = Form(),
    password: str = Form(min_length=8)
):
    return adc.create_admin(db, name, email, password)
