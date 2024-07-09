from sqlalchemy import  Column, Integer, String, DateTime, Enum
import enum
# from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
from App.Http.Providers.database import Base, db
# from App.Http.Models.User import User
from App.Http.Models.ProjectAssignment import ProjectAssignment

# from TaskApp.App.Http.Providers.database import Base, db
# from pydantic import BaseModel
# from typing import Optional



class Project(Base):
    __tablename__ = "projects"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    name = Column(String(100), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    project_assignment = relationship("ProjectAssignment", back_populates="project", uselist=False)

    def __init__(self, user = {}):
        self.db = db()

        self.name = user.get('name', '')
        self.deleted_at = user.get('deleted_at','')
        self.created_at = user.get('created_at','')
        self.updated_at = user.get('updated_at','')

    def table(self):
        return self.db.query(Project)
      