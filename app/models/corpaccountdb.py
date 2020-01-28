from sqlalchemy import Column, String, Integer
from app import app, Base, engine
from .base import BaseModel

class CorperateAccountDB(BaseModel):

    __tablename__ = "corperateaccounts"

    accountnumber = Column(String)
    accountname = Column(String)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
