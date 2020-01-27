from sqlalchemy import String, Column, Boolean, Integer, Date, ForeignKey
from app import Base, engine
from .base import BaseModel
from sqlalchemy.orm import relationship
from .userdb import UserDB
from .idtypedb import IdTypeDB
from .roledb import RoleDB
from sqlalchemy.dialects.postgresql import UUID

class UserRoleDB(BaseModel):

    __tablename__ = "userroles"

    userid = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    roleid = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    status = Column(String)
    usertype = relationship("UserDB", back_populates="userroles")
    roletype = relationship("RoleDB", back_populates="userroles")
    

UserDB.userroles = relationship("UserRoleDB", order_by = UserRoleDB.id, back_populates="usertype")
RoleDB.userroles = relationship("UserRoleDB", order_by=UserRoleDB.id, back_populates='roletype')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
