from sqlalchemy import Column, Integer, String, Date
from app import app, Base
from app import engine
from .base import BaseModel


class UserDB(BaseModel):

    __tablename__ = "user"

    name = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return "<Sale(city_name='%s')>" % (self.phone)


Base.metadata.create_all(engine)
