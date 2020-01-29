from sqlalchemy import Column, String, Integer
from app import engine, Base
from .base import BaseModel

class BankCodeDB(BaseModel):

    __tablename__ = "bankcodes"

    bankname = Column(String)
    universalbranchcode = Column(String)

Base.metadata.create_all(engine)