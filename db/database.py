from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from google.cloud.sql.connector import Connector, IPTypes
from dotenv import load_dotenv

load_dotenv()

db_host = os.environ["INSTANCE_HOST"]  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
db_port = os.environ["DB_PORT"]  # e.g. 3306
connection_name = os.environ['CONNECTION_NAME']


# Python Connector database connection function
def getconn():
    with Connector() as connector:
        conn = connector.connect(
            connection_name, # Cloud SQL Instance Connection Name
            "pymysql",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type= IPTypes.PUBLIC  # IPTypes.PRIVATE for private IP
        )
    return conn

DATABASE_URL = "mysql+pymysql://"

engine = create_engine(DATABASE_URL, creator=getconn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()