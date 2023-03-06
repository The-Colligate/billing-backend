from pathlib import Path
from enum import Enum

home = Path(__file__).resolve().parent  # store path to home


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
