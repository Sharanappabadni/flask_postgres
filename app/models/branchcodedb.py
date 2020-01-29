from sqlalchemy import Column, String, Integer, ForeignKey, Text
from app import Base, engine
from .base import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from app.models import BankCodeDB
from sqlalchemy.orm import relationship

class BranchCodeDB(BaseModel):

    __tablename__ = "branchcodes"

    bankcode = Column(UUID(as_uuid=True), ForeignKey("bankcodes.id"))
    branchname = Column(String)
    branchaddress = Column(Text)
    banktype = relationship("BankCodeDB", back_populates="branchcodes")

BankCodeDB.branchcodes = relationship("BranchCodeDB", order_by=BranchCodeDB.id, back_populates="banktype")
Base.metadata.create_all(engine)