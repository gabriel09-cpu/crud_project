from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlite3

BASE_DE_DADOS = "sqlite:///./books.db"
engine = create_engine(BASE_DE_DADOS, connect_args={
    "check_same_thread":False
})

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()