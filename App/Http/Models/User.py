from sqlalchemy import  Column, Integer, String, DateTime, Enum
import enum
# from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import validates
from App.Http.Providers.database import Base, db
# from TaskApp.App.Http.Providers.database import Base, db
# from pydantic import BaseModel
# from typing import Optional

class UserRoles(enum.Enum):
    admin = 'admin'
    user = 'user'

class UserStatus(enum.Enum):
    active = 'active'
    in_active = 'in_active'

class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    name = Column(String(100), nullable=False)
    second_name = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False)
    status = Column(Enum(UserStatus), nullable=False, default=UserStatus.active.value)
    role = Column(Enum(UserRoles), nullable=False, default=UserRoles.user.value)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    

    def __init__(self, user = {}):
        self.db = db()

        self.name = user.get('name', '')
        self.second_name = user.get('second_name' , '')
        self.email = user.get('email', '')
        self.password = user.get('password', '')
        self.status = user.get('status', UserStatus.active.value)
        self.role = user.get('role',UserRoles.user.value)
        self.deleted_at = user.get('deleted_at','')
        self.created_at = user.get('created_at','')
        self.updated_at = user.get('updated_at','')

    # def __init__(self, user:class):
    #     self.db = db()
    #     self = user


    @validates('role')
    def validate_role(self, key, role):
        if not isinstance(role, str) or role not in [r.value for r in UserRoles]:
            raise ValueError(f"Invalid role: {role}")
        return role

    @validates('status')
    def validate_status(self, key, status):
        if not isinstance(status, str) or status not in [s.value for s in UserStatus]:
            raise ValueError(f"Invalid status: {status}")
        return status
    def table(self):
        return self.db.query(User)
    
