from App.Http.Controllers.Controller import Controller
from fastapi import Depends, Form, Security
from App.Http.RequestForms.Auth import Token
from App.Http.RequestForms.User import ProfileForm
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider

from App.Http.Models.Task import Task

from datetime import datetime

from sqlalchemy import update

from App.Http.RequestForms.Tasks import UpdateForm, StoreForm

class Tasks(Controller):

    def index(self,project_id:int, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        return (
            Task().table()
            .filter(Task.deleted_at.is_(None))
            .filter(Task.project_id == project_id)
            .all()
            )
    
    def store(self,project_id:int, task_form: StoreForm.StoreForm, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        payload = {
            "title": task_form.title,
            "description": task_form.description,
            "status": task_form.status,
            "project_id": project_id,
            "assignee_id": task_form.assignee_id,
            "parent_id": task_form.parent_id,
            'deleted_at' : None,
            'created_at' : datetime.now(),
            'updated_at' : None,
        }

        task = Task(payload)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return {
            'msg':{
                'success':'Task created Successfully!',
            },
            'user':task
        }
        
    def update(self,project_id:int, task_id: int , task_form: UpdateForm.UpdateForm, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        task = (Task().table()
        .filter(Task.id == task_id)
        .filter(Task.project_id == project_id)
        .first())
        # return user
    
        if task:
            payload = {
                "title": task_form.title,
                "description": task_form.description,
                "status": task_form.status,
                # "project_id": project_id,
                # "assignee_id": task_form.assignee_id,
                # "parent_id": task_form.parent_id,
                'updated_at' : datetime.now()
            }
            # return user, payload, user_id
            # ----------------------------------------------------------------
            um = Task()
            stmt = (
                um.table()
                .filter(Task.id == task_id)
                .filter(Task.project_id == project_id)
                .update(payload)
            )
            um.db.commit()

            if stmt:
                return {
                    'msg':{
                        'success':'Task updated Successfully!',
                    },
                    'user': (
                        Task().table()
                        .filter(Task.id == task_id)
                        .filter(Task.project_id == project_id)
                        .first()
                    )
                }

            return payload, stmt
        else:
            return {
                'msg':{
                    'error':'No Task Found with this id!',
                },
                'task_id': task_id
            }
    def delete(self, project_id:int, task_id: int, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        task_model = Task()
        user_data = (task_model.table()
        .filter(Task.project_id == project_id)
        .filter(Task.id == task_id).first())
        # return user
        if(user_data):
            payload = {
                'deleted_at' : datetime.now(),
            }
            stmt = (task_model.table()
            .filter(Task.project_id == project_id)
            .filter(Task.id == task_id).update(payload))
            task_model.db.commit()
            
            if stmt:
                return {
                    'msg':{
                        'success':'Task deleted Successfully!',
                    },
                    'user': task_model.table().filter(Task.id == task_id).first()
                }

        else:
            return {
                'msg':{
                    'error':'No Task Found with this id!',
                },
                'task_id': task_id
            }
        
    # def assign(self, task_id: int,users: AssignUsersForm.AssignUsersForm , token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
    #     task_assignments = []
    #     for user_id in users.users:
    #         payload = {
    #             "task_id":task_id,
    #             "user_id":user_id,
    #             'deleted_at' : None,
    #             'created_at' : datetime.now(),
    #             'updated_at' : None,
    #         }
    #         already_exist = (
    #             Task()
    #             .table()
    #             .filter(Task.deleted_at.is_(None))
    #             .filter(Task.user_id == user_id)
    #             .filter(Task.task_id == task_id)
    #             .first()
    #         )
    #         if(already_exist):
    #             task_assignments.append(payload)
    #             continue

            
    #         task_assignment = Task(payload)
    #         self.db.add(task_assignment)
    #         self.db.commit()
    #         self.db.refresh(task_assignment)
    #         task_assignments.append(payload)

    #     return {
    #         'msg':{
    #             'success':'Task Assigned Successfully!',
    #         },
    #         'user': task_assignments
    #     }
        
    