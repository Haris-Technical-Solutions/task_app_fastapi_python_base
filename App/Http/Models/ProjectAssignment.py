from sqlalchemy import  Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import enum
# from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import validates
from App.Http.Providers.database import Base, db

# from App.Http.Models.User import User
# from App.Http.Models.Project import Project

# from TaskApp.App.Http.Providers.database import Base, db
# from pydantic import BaseModel
# from typing import Optional



class ProjectAssignment(Base):
    __tablename__ = "project_assignments"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)

    # ForeignKey
    project_id = Column(Integer, ForeignKey('projects.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)


    # relationships
    user = relationship("User", back_populates="project_assignments")
    project = relationship("Project", back_populates="project_assignments")

    def __init__(self, user = {}):
        self.db = db()

        self.project_id = user.get('project_id', '')
        self.user_id = user.get('user_id', '')

        self.deleted_at = user.get('deleted_at','')
        self.created_at = user.get('created_at','')
        self.updated_at = user.get('updated_at','')

    def table(self):
        return self.db.query(ProjectAssignment)
      