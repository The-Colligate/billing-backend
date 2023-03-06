from fastapi import APIRouter, UploadFile, Depends, Query, File
from db.database import get_db
from controllers import fileC as fc
from sqlalchemy.orm import Session
from datetime import datetime
from utils import Plan, Month


router = APIRouter(prefix="/file")


@router.post(
    "/upload", description="Upload the spreadsheet file for a given month+year"
)
def upload(
    *,
    db: Session = Depends(get_db),
    plan: Plan,
    month: Month,
    year: int = Query(default=datetime.now().year),
    excelfile: UploadFile = File()
):
    return fc.initiate_upload(db, plan, month, year, excelfile)


@router.get("/recent")
def recent_transactions(*, db: Session = Depends(get_db), limit: int):
    return fc.pull_all(db, limit)


# @router.get(
#     "/resolve",
#     tags=["to delete, for dev"],
#     description="""utility function. Upload files, resolve clients and their ids, populate the clients table, show uploaded months""",
# )
# def refresh(db: Session = Depends(get_db)):
#     return fc.resolve_all(db)
