from App.Http.Controllers.Controller import Controller
from fastapi import Depends, Form, Security
from App.Http.RequestForms.Auth import Token
from App.Http.RequestForms.User import ProfileForm
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider

from App.Http.Models.TaskComment import TaskComment

from datetime import datetime

from sqlalchemy import update

from App.Http.RequestForms.TaskComments import UpdateForm, StoreForm

class TaskComments(Controller):

    def index(self,project_id:int, task_id: int , token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        return (
            TaskComment().table()
            .filter(TaskComment.deleted_at.is_(None))
            .filter(TaskComment.task_id == task_id)
            .all()
            )
    
    def store(self,project_id:int, task_id: int , task_form: StoreForm.StoreForm, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        payload = {
            "content": task_form.content,
            "task_id": task_id,
            "parent_id": task_form.parent_id,

            'deleted_at' : None,
            'created_at' : datetime.now(),
            'updated_at' : None,
        }

        task = TaskComment(payload)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return {
            'msg':{
                'success':'TaskComment added Successfully!',
            },
            'user':task
        }
        
    def update(self,project_id:int, task_id: int, comment_id: int , task_form: UpdateForm.UpdateForm, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        task = (TaskComment().table()
        .filter(TaskComment.id == comment_id)
        .filter(TaskComment.task_id == task_id)
        .first())
        # return user
    
        if task:
            payload = {
                "content": task_form.content,
                # "task_id": task_id,
                # "parent_id": task_form.parent_id,

                'updated_at' : datetime.now()
            }

            # return user, payload, user_id
            # ----------------------------------------------------------------
            um = TaskComment()
            stmt = (
                um.table()
                .filter(TaskComment.id == comment_id)
                .filter(TaskComment.task_id == task_id)
                .update(payload)
            )
            um.db.commit()

            if stmt:
                return {
                    'msg':{
                        'success':'TaskComment updated Successfully!',
                    },
                    'user': (
                        TaskComment().table()
                        .filter(TaskComment.id == comment_id)
                        .filter(TaskComment.task_id == task_id)
                        .first()
                    )
                }

            return payload, stmt
        else:
            return {
                'msg':{
                    'error':'No TaskComment Found with this id!',
                },
                'task_id': task_id
            }
    def delete(self, project_id:int, task_id: int, comment_id: int, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        task_model = TaskComment()
        task_comment_data = (task_model.table()
        .filter(TaskComment.task_id == task_id)
        .filter(TaskComment.id == comment_id).first())
        
        if(task_comment_data):

            task_comment_child_data = (task_model.table()
            .filter(TaskComment.task_id == task_id)
            .filter(TaskComment.parent_id == comment_id).first())
            # return user
            if(task_comment_child_data):
                return {
                    'msg':{
                        'error':'Parent TaskComment cannot be deleted!',
                    },
                    'comment_id': comment_id
                }
            payload = {
                'deleted_at' : datetime.now(),
            }
            stmt = (task_model.table()
            .filter(TaskComment.task_id == task_id)
            .filter(TaskComment.id == comment_id)
            .update(payload))
            task_model.db.commit()
            
            if stmt:
                return {
                    'msg':{
                        'success':'TaskComment deleted Successfully!',
                    },
                    'user': task_model.table().filter(TaskComment.id == comment_id).first()
                }

        else:
            return {
                'msg':{
                    'error':'No TaskComment Found with this id!',
                },
                'comment_id': comment_id
            }
        