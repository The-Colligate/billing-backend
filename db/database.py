from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

<<<<<<< HEAD
from dotenv  import load_dotenv


load_dotenv()

DATABASE_URL = os.environ["PROD_DATABASE_URL"]
=======
# DATABASE_URL = os.environ["PROD_DATABASE_URL"]
DATABASE_URL = 'sqlite:///./billing-prod.db'
>>>>>>> 3114c4f31779bf747f8f2edff518d805d6364aba

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
