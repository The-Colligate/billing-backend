from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, DECIMAL
from sqlalchemy.orm import relationship, backref


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    tier = Column(Integer)
    cac_id = Column(String(20))
    tin_id = Column(String(20))
    address = Column(String(500))
    website = Column(String(500))
    description = Column(String(255))
    admin_id = Column(Integer, ForeignKey("admins.id"))
    focal_point_id = Column(Integer, ForeignKey("FocalPoints.id"))
    created = Column(DateTime)
    active = Column(Boolean)

    # admin = relationship('Admin', foreign_keys=[admin_id])
    focal_point = relationship(
        "FocalPoint", backref=backref("client"), foreign_keys=[focal_point_id]
    )


class FocalPoint(Base):
    __tablename__ = "FocalPoints"

    id = Column(Integer, index=True, primary_key=True)

    name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    client_id = Column(Integer, ForeignKey("clients.id"), unique=True)


class Sub(Base):
    # store relationships between children and parent companies
    __tablename__ = "relationships"

    id = Column(Integer, primary_key=True)

    child_id = Column(Integer, ForeignKey("clients.id"))
    parent_id = Column(Integer, ForeignKey("clients.id"))

    child = relationship("Client", foreign_keys=[child_id])
    parent = relationship("Client", foreign_keys=[parent_id])


class Admin(Base):
    # define admins for the system
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    level = Column(Integer)
    hashed_password = Column(String(255))


class Voice(Base):
    # store ledger for voice services
    __tablename__ = "voice"

    id = Column(Integer, primary_key=True, index=True)

    client_name = Column(String(255))
    client_id = Column(ForeignKey("clients.id"))
    msisdn = Column(Integer)
    balance_forward = Column(DECIMAL)
    current_invoice = Column(DECIMAL)
    last_payment = Column(DECIMAL)
    outstanding_debt = Column(DECIMAL)
    month = Column(String(255))
    year = Column(Integer)


class Data(Base):
    # store ledger for data services
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)

    client_name = Column(String(255))
    client_id = Column(ForeignKey("clients.id"))
    business_unit = Column(String(255))
    balance = Column(DECIMAL)
    last_invoice = Column(DECIMAL)
    last_payment = Column(DECIMAL)
    debit = Column(DECIMAL)
    credit = Column(DECIMAL)
    currency = Column(String)
    month = Column(String)
    year = Column(Integer)


class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, index=True)
    client_id = Column(ForeignKey("clients.id"))
    statement_date = Column(DateTime)
    billing_start = Column(DateTime)
    billing_end = Column(DateTime)
    due_date = Column(DateTime)
    amount_due = Column(DECIMAL)
    services = Column(String(2000))

    client = relationship("Client", foreign_keys=[client_id])

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String(100))
    rate = Column(DECIMAL)
