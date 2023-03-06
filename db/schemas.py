from pydantic import BaseModel, EmailStr
from datetime import datetime


class AdminBase(BaseModel):
    id: int = None


class Admin(AdminBase):
    name: str
    email: EmailStr
    level: int

    class Config:
        orm_mode = True


class FocalPoint(BaseModel):
    name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True


# class FocalPoint(FocalPointBase):
#     id: int = None
#     client_id: int


class ClientBase(BaseModel):
    name: str
    tier: int = 1


class ClientDetails(ClientBase):
    """used to create a client"""

    cac_id: str = None
    tin_id: str = None
    address: str = None
    website: str = None
    description: str = None

    class Config:
        orm_mode = True


class Client(ClientDetails):
    """the schema for loading the user on get"""

    created: datetime
    active: bool
    focal_point: FocalPoint = None


class ClientID(ClientBase):
    """summary of each client, for the clients page"""

    id: int
    active: bool
    admin_id: int = None

    class Config:
        orm_mode = True


class VoiceCreate(BaseModel):
    client_name: str
    client_id: int
    msisdn: int
    balance_forward: float
    current_invoice: float
    last_payment: float
    outstanding_debt: float
    month: str
    year: int


class Voice(VoiceCreate):
    id: int


class DataCreate(BaseModel):
    customer_id: int
    business_unit: int
    balance: float
    last_invoice: float
    last_payment: float
    debit: float
    credit: float
    currency: str
    month: str
    year: int


class Data(DataCreate):
    id: int
