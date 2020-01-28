from sqlalchemy import Column, String, Integer
from app import app, Base, engine
from .base import BaseModel

class IdTypeDB(BaseModel):

    __tablename__ = 'IDTypes'

    name = Column(String)
    idnumber = Column(String)

Base.metadata.create_all(engine)

