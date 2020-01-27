from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from app import app, Base
from app import engine
from .base import BaseModel
from sqlalchemy.orm import relationship
from .idtypedb import IdTypeDB
from sqlalchemy.dialects.postgresql import UUID

class UserDB(BaseModel):

    __tablename__ = "users"

    username = Column(String)
    email = Column(String)
    phone = Column(String)
    gender = Column(String)
    firstname = Column(String)
    surename = Column(String)
    DOB = Column(Date)
    idnumber = Column(UUID(as_uuid=True), ForeignKey('IDTypes.id'))
    idtype = relationship("IdTypeDB", back_populates = "users")

    def __repr__(self):
        return "<User (user details='%s')>" % (self.phone)

IdTypeDB.users = relationship("UserDB", order_by = UserDB.id, back_populates = "idtype")
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
