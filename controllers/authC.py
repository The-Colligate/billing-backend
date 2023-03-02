from passlib.context import CryptContext
from sqlalchemy.orm import Session
from pydantic import EmailStr
from fastapi import HTTPException, status
from db import models
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from datetime import timedelta, datetime

load_dotenv()

EXPIRY_HOURS = int(os.environ["ACCESS_TOKEN_EXPIRE_HOURS"])
ALGORITHM = os.environ["ALGORITHM"]
SECRET_KEY = os.environ["SECRET_KEY"]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashp(password):
    return pwd_context.hash(password)


def verify_hash(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_admin(db: Session, email: EmailStr, password: str):
    db_admin = db.query(models.Admin).filter(models.Admin.email == email).first()

    if (not db_admin) or (not (verify_hash(password, db_admin.hashed_password))):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return db_admin


def authenticate_client(db: Session):
    ...


def create_access_token(data: dict):
    to_encode = data.copy()
    expiry_time = datetime.now() + timedelta(hours=EXPIRY_HOURS)

    to_encode.update({"exp": expiry_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def signup(db: Session, username: str, password: str):
    ...
