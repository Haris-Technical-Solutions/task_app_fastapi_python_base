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



class TaskComment(Base):
    __tablename__ = "task_comments"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)

    content = Column(String(100), nullable=True)

    parent_id = Column(Integer, ForeignKey('task_comments.id'), nullable=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), nullable=True)

    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    # relationships
    task = relationship("Task", back_populates="comments")
    parent = relationship("TaskComment")

    # back relation


    def __init__(self, user = {}):
        self.db = db()

        self.content = user.get('content', '')
        self.task_id = user.get('task_id', '')
        self.parent_id = user.get('parent_id', '')

        self.deleted_at = user.get('deleted_at','')
        self.created_at = user.get('created_at','')
        self.updated_at = user.get('updated_at','')

    def table(self):
        return self.db.query(TaskComment)
      