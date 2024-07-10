from App.Http.Controllers.Controller import Controller
from fastapi import Depends, Form, Security
from App.Http.RequestForms.Auth import Token
from App.Http.RequestForms.User import ProfileForm
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider

from App.Http.Models.Project import Project
from App.Http.Models.ProjectAssignment import ProjectAssignment

from datetime import datetime

from sqlalchemy import update

from App.Http.RequestForms.Projects import UpdateForm, StoreForm, AssignUsersForm

class AdminProjects(Controller):

    def index(self, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        return Project().table().filter(Project.deleted_at.is_(None)).all()
    
    def store(self, project_form: StoreForm.StoreForm, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        payload = {
            'name' : project_form.name,
            'deleted_at' : None,
            'created_at' : datetime.now(),
            'updated_at' : None,
        }

        project = Project(payload)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return {
            'msg':{
                'success':'Project created Successfully!',
            },
            'user':project
        }
        
    def update(self,project_id: int , project_form: UpdateForm.UpdateForm, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        project = Project().table().filter(Project.id == project_id).first()
        # return user
    
        if project:
            payload = {
                "name": project_form.name,
                'updated_at' : datetime.now()
            }
            # return user, payload, user_id
            # ----------------------------------------------------------------
            um = Project()
            stmt = (
                um.table()
                .filter(Project.id == project_id)
                .update(payload)
            )
            um.db.commit()

            if stmt:
                return {
                    'msg':{
                        'success':'Project updated Successfully!',
                    },
                    'user': (
                        Project().table()
                        .filter(Project.id == project_id)
                        .first()
                    )
                }

            return payload, stmt
        else:
            return {
                'msg':{
                    'error':'No Project Found with this id!',
                },
                'project_id': project_id
            }
    def delete(self,project_id: int, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        user_model = Project()
        user_data = user_model.table().filter(Project.id == project_id).first()
        # return user
        if(user_data):
            payload = {
                'deleted_at' : datetime.now(),
            }
            stmt = user_model.table().filter(Project.id == project_id).update(payload)
            user_model.db.commit()
            
            if stmt:
                return {
                    'msg':{
                        'success':'Project deleted Successfully!',
                    },
                    'user': user_model.table().filter(Project.id == project_id).first()
                }

        else:
            return {
                'msg':{
                    'error':'No Project Found with this id!',
                },
                'project_id': project_id
            }
        
    def assign(self, project_id: int,users: AssignUsersForm.AssignUsersForm , token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        project_assignments = []
        for user_id in users.users:
            payload = {
                "project_id":project_id,
                "user_id":user_id,
                'deleted_at' : None,
                'created_at' : datetime.now(),
                'updated_at' : None,
            }
            already_exist = (
                ProjectAssignment()
                .table()
                .filter(ProjectAssignment.deleted_at.is_(None))
                .filter(ProjectAssignment.user_id == user_id)
                .filter(ProjectAssignment.project_id == project_id)
                .first()
            )
            if(already_exist):
                project_assignments.append(payload)
                continue

            
            project_assignment = ProjectAssignment(payload)
            self.db.add(project_assignment)
            self.db.commit()
            self.db.refresh(project_assignment)
            project_assignments.append(payload)

        return {
            'msg':{
                'success':'Project Assigned Successfully!',
            },
            'user': project_assignments
        }
        
    