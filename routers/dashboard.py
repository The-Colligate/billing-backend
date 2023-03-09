from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from controllers import dashboardC as dc
from utils import PlanExt, Plan

router = APIRouter(tags=["dashboard"])


@router.get("/count_clients/")
def count_clients(*, db: Session = Depends(get_db), plan: PlanExt):
    return dc.count_clients(db, plan)


@router.get("/count_invoices/")
def count_invoices(*, db: Session = Depends(get_db), plan: PlanExt):
    return dc.count_invoices(db, plan)


@router.get("/total-revenue/")
def calc_revenue(*, db: Session = Depends(get_db), plan: PlanExt):
    return dc.calc_revenue(db, plan)


@router.get("/loyalty/", deprecated=True)
def calc_loyalty(*, db: Session = Depends(get_db), plan: PlanExt):
    return dc.calc_loyalty(db, plan)


@router.get("/recent_invoices/")
def recent_invoices(*, db: Session = Depends(get_db), plan: Plan, limit: int = 10):
    return dc.recent_invoices(db, plan, len=limit)


@router.get("/outstanding_debt")
def get_debt(*, db: Session = Depends(get_db), plan: PlanExt):
    return dc.get_debt(db, plan)
