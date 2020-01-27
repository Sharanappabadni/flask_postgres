from sqlalchemy import Column, Integer, String, Date, Boolean
from app import Base, engine
from .base import BaseModel


class RoleDB(BaseModel):

    __tablename__ = "roles"

    rolecode = Column(Integer, unique=True)
    roledesc = Column(String)
    status = Column(String)

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)