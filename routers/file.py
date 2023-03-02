from fastapi import APIRouter, UploadFile, Depends, Query, File
from db.database import get_db
from enum import Enum
from controllers import fileC as fc
from sqlalchemy.orm import Session
from datetime import datetime


router = APIRouter(prefix="/file")


class Plan(str, Enum):
    voice = "voice"
    data = "data"


class Month(str, Enum):
    january = "January"
    february = "February"
    march = "March"
    april = "April"
    may = "May"
    june = "June"
    july = "July"
    august = "August"
    september = "September"
    october = "October"
    november = "November"
    december = "December"


@router.post(
    "/upload", description="Upload the spreadsheet file for a given month+year"
)
def upload(
    *,
    db: Session = Depends(get_db),
    service: Plan,
    month: Month,
    year: int = Query(default=datetime.now().year),
    xlfile: UploadFile = File()
):
    return fc.initiate_upload(db, service, month, year, xlfile)


@router.get("/recent")
def recent_transactions(*, db: Session = Depends(get_db), limit: int):
    return fc.pull_all(db, limit)


@router.get(
    "/resolve",
    tags=["to delete, for dev"],
    description="""utility function. Upload files, resolve clients and their ids, populate the clients table, show uploaded months""",
)
def refresh(db: Session = Depends(get_db)):
    return fc.resolve_all(db)
