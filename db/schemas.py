from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, date, timedelta
from decimal import Decimal


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


class ClientInvoice(ClientBase):
    """name, tier and address of client, for creating invoice"""

    address: str = None

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


class ServiceBase(BaseModel):
    service: str

class ServiceInvoice(ServiceBase):
    '''Used to add a service to the invoice'''
    quantity: float

    class Config:
        orm_mode = True

class ServiceEdit(ServiceBase):
    rate: Decimal


class InvoiceCreate(BaseModel):
    statement_date: date = Field(default_factory=date.today)
    billing_start: date
    billing_end: date
    due_date: date
    amount_due: Decimal = 0.0


class Invoice(BaseModel):
    services: list[ServiceInvoice]
    client_id: int
    invoice_id: int
    bill_to: ClientInvoice