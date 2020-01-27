from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy_utils import UUIDType
from sqlalchemy import Column, Date
import datetime

from app import app, Base

class BaseModel(Base):
    __abstract__ = True

    id = Column(
        UUIDType(binary=True),
        primary_key = True,
        default = uuid.uuid1
    )

    created_on = Column(
        Date,
        nullable=False,
        default=datetime.datetime.now()
    )