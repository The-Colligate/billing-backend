from pydantic import BaseModel, EmailStr


class AdminBase(BaseModel):
    id: int = None


class Admin(AdminBase):
    name: str
    email: EmailStr
    level: int

    class Config:
        orm_mode = True


class ClientCreate(BaseModel):
    tier: int = 1
    name: str
    cac_id: str = None
    tin_id: str = None
    address: str = None
    website: str = None
    description: str = None
    admin_id: AdminBase = 1


class Client(ClientCreate):
    id: int = None

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
