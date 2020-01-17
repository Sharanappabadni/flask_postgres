from sqlalchemy import Column, Integer, String, Date
from app import app, Base
from app import engine


class UserDB(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    createdon = Column(Date)

    def __repr__(self):
        return "<Sale(city_name='%s')>" % (self.phone)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
