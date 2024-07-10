from sqlalchemy import  Column, Integer, String, DateTime, Enum, ForeignKey
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



class Task(Base):
    __tablename__ = "tasks"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)

    title = Column(String(100), nullable=False)
    description = Column(String(100), nullable=True)
    status = Column(String(100), nullable=False)

    project_id = Column(Integer, ForeignKey('projects.id') , nullable=False)
    assignee_id = Column(Integer, ForeignKey('users.id') , nullable=False)
    parent_id = Column(Integer, ForeignKey('tasks.id'), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    # relationships
    assignee = relationship("User", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")
    parent = relationship("Task")

    # back relation
    # tasks = relationship("Task", back_populates="parent", uselist=False)
    comments = relationship("TaskComment", back_populates="task", uselist=False)


    def __init__(self, user = {}):
        self.db = db()

        self.title = user.get('title', '')
        self.description = user.get('description', '')
        self.status = user.get('status', '')
        self.project_id = user.get('project_id', '')
        self.assignee_id = user.get('assignee_id', '')
        self.parent_id = user.get('parent_id', '')

        self.deleted_at = user.get('deleted_at','')
        self.created_at = user.get('created_at','')
        self.updated_at = user.get('updated_at','')

    def table(self):
        return self.db.query(Task)
      