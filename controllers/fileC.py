import pandas as pd
from sqlalchemy.orm import Session
from db import models, schemas


def initiate_upload(db: Session, service: str, month: str, year: int, xlfile):
    df = pd.read_excel(xlfile.file)
    df["month"] = month
    df["year"] = year
    if service.value == "voice":
        upload_voice_transactions(db, df)
    if service.value == "data":
        upload_data_transactions(db, df)

    return f"{df.shape[0]} rows in '{xlfile.filename}' uploaded to '{service.value.title()}' table✅"


def upload_voice_transactions(db: Session, df: pd.DataFrame):
    # preprocessing steps to perform rename, cast and drop operations
    df.rename(
        columns={
            "Name": "client_name",
            "MSISDN": "msisdn",
            "Balance Forward": "balance_forward",
            "Current Invoice": "current_invoice",
            "Last Payment": "last_payment",
            "Outstanding Debt": "outstanding_debt",
        },
        inplace=True,
    )

    # remove commas, convert to float
    df.balance_forward = df.balance_forward.str.replace(",", "").astype(float)
    df.current_invoice = df.current_invoice.str.replace(",", "").astype(float)
    df.last_payment = df.last_payment.str.replace(",", "").astype(float)
    df.outstanding_debt = df.outstanding_debt.str.replace(",", "").astype(float)

    # drop column
    df.drop(columns="S/N", inplace=True)

    # turn into a dict that I can easily instantiate as a `Voice` model
    voice_dict = df.to_dict(orient="records")
    voice_records = [models.Voice(**i) for i in voice_dict]

    for record in voice_records:
        # if the client doesn't exist, add them
        client = (
            db.query(models.Client)
            .filter(models.Client.name == record.client_name)
            .first()
        )
        if not client:
            client = models.Client(
                **schemas.ClientBase(name=record.client_name).dict(), active=True
            )
            db.add(client)
            db.commit()
            db.refresh(client)  # refresh so we can get the client's id

        record.client_id = (
            client.id
        )  # assign voice record to the id of the right client

        # add voice ledger record to voice table
        db.add(record)

    db.commit()


def get_curr(ser):
    """function to get the currency of a row"""
    if str(ser)[-3:] == "USD":
        return "USD"
    else:
        return "NGN"


def upload_data_transactions(db: Session, df: pd.DataFrame):
    # preprocessing steps to perform rename, cast and drop operations
    df.rename(
        columns={
            "Customer": "client_name",
            "Business Unit": "business_unit",
            "Balance": "balance",
            "Last Invoice": "last_invoice",
            "Last payment": "last_payment",
            "Debit": "debit",
            "Credit": "credit",
        },
        inplace=True,
    )

    strip_ngn = lambda x: str(x).rstrip(" NGN")  # function to rstrip naira
    strip_usd = lambda x: str(x).rstrip(" USD")  # function to rstrip dollar

    df["currency"] = df["balance"].apply(get_curr)  # get currency

    # remove commas, convert to float, strip currency unit
    df.balance = (
        df.balance.str.replace(",", "").apply(strip_ngn).apply(strip_usd).astype(float)
    )
    df.last_invoice = (
        df.last_invoice.str.replace(",", "")
        .apply(strip_ngn)
        .apply(strip_usd)
        .astype(float)
    )
    df.last_payment = (
        df.last_payment.str.replace(",", "")
        .apply(strip_ngn)
        .apply(strip_usd)
        .astype(float)
    )
    df.debit = df.debit.str.replace(",", "").astype(float)
    df.credit = df.credit.str.replace(",", "").astype(float)

    # drop column
    df.drop(columns="S/N", inplace=True)

    # turn into a dict that I can easily instantiate as a `Voice` model
    data_dict = df.to_dict(orient="records")
    data_records = [models.Data(**i) for i in data_dict]

    for record in data_records:
        # if the client doesn't exist, add them
        client = (
            db.query(models.Client)
            .filter(models.Client.name == record.client_name)
            .first()
        )
        if not client:
            client = models.Client(
                **schemas.ClientBase(name=record.client_name).dict(), active=True
            )
            db.add(client)
            db.commit()
            db.refresh(client)  # refresh so we can get the client's id

        record.client_id = client.id  # assign data record to the id of the right client

        # add data ledger record to data table
        db.add(record)

    db.commit()
