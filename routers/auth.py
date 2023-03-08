from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from controllers import authC as ac
from db.database import get_db
from jose import jwt, JWTError
import os
from utils import credentials_exception

router = APIRouter(tags=["auth"])

admin_auth = OAuth2PasswordBearer(tokenUrl="/admin/login")

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]


@router.post("/admin/login")
def admin_login(
    *, db: Session = Depends(get_db), form_data=Depends(OAuth2PasswordRequestForm)
):
    db_admin = ac.authenticate_admin(db, form_data.username, form_data.password)
    access_token = ac.create_access_token(data={"sub": db_admin.email})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/current_admin")
def current_admin(*, db: Session = Depends(get_db), token: str = Depends(admin_auth)):
    try:
        jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception


@router.post("/client/login", deprecated=True)
def client_login(
    *, db: Session = Depends(get_db), form_data=Depends(OAuth2PasswordRequestForm)
):
    db_client = ac.authenticate_client(db, form_data.username, form_data.password)
