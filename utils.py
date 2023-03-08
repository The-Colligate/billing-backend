from pathlib import Path
from enum import Enum
from fastapi.exceptions import HTTPException
from fastapi import status

home = Path(__file__).resolve().parent  # store path to home

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="incorrect credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


class Plan(str, Enum):
    voice = "voice"
    data = "data"


class PlanExt(str, Enum):
    all = "all"
    voice = "voice"
    data = "data"


class Month(str, Enum):
    January = "January"
    February = "February"
    March = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September = "September"
    October = "October"
    November = "November"
    December = "December"


class Tier(str, Enum):
    Silver = 1
    Gold = 2
    Platinum = 3
