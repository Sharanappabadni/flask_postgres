from sqlalchemy import Column, Integer, String, Date
from app import app, Base

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(Integer)
    createdon = Column(Date)
