from .database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tier = Column(Integer)
    cac_id = Column(String)
    tin_id = Column(String)
    address = Column(String)
    website = Column(String)
    description = Column(String)
    admin_id = Column(Integer, ForeignKey("admins.id"))
    focal_point_id = Column(Integer, ForeignKey("FocalPoints.id"))
    active = Column(Boolean)

    # admin = relationship('Admin', foreign_keys=[admin_id])
    focal_point = relationship(
        "FocalPoint", backref=backref("client"), foreign_keys=[focal_point_id]
    )


class FocalPoint(Base):
    __tablename__ = "FocalPoints"

    id = Column(Integer, index=True, primary_key=True)

    name = Column(String)
    email = Column(String)
    phone = Column(String)
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
    name = Column(String)
    email = Column(String, unique=True)
    level = Column(Integer)
    hashed_password = Column(String)


class Voice(Base):
    # store ledger for voice services
    __tablename__ = "voice"

    id = Column(Integer, primary_key=True, index=True)

    client_name = Column(String)
    client_id = Column(ForeignKey("clients.id"))
    msisdn = Column(Integer)
    balance_forward = Column(Float)
    current_invoice = Column(Float)
    last_payment = Column(Float)
    outstanding_debt = Column(Float)
    month = Column(String)
    year = Column(Integer)


class Data(Base):
    # store ledger for data services
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)

    client_name = Column(String)
    client_id = Column(ForeignKey("clients.id"))
    business_unit = Column(String)
    balance = Column(Float)
    last_invoice = Column(Float)
    last_payment = Column(Float)
    debit = Column(Float)
    credit = Column(Float)
    currency = Column(String)
    month = Column(String)
    year = Column(Integer)


#     # customer = relationship('')
