from App.Http.Controllers.Controller import Controller
from fastapi import Depends, Form, Security
from App.Http.RequestForms.Auth import Token
from App.Http.RequestForms.User import ProfileForm
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider

from App.Http.Models.Project import Project
from App.Http.Models.User import User
from App.Http.Models.ProjectAssignment import ProjectAssignment
from App.Http.Controllers.Auth import Auth

from datetime import datetime

from sqlalchemy import update, select 
from sqlalchemy.orm import load_only, lazyload, joinedload, defaultload

from App.Http.RequestForms.Projects import UpdateForm, StoreForm, AssignUsersForm

class Projects(Controller):

    def index(self, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        user = Auth().user(token)
        if user:
            return( 
                Project()
                .table()
                .join(ProjectAssignment)
                .filter(ProjectAssignment.user_id == user.id)
                .filter(Project.deleted_at.is_(None))
                .all()
            )
    def show(self,project_id: int, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
        user = Auth().user(token)
        if user:
            # u = (User().table()
            # .join(ProjectAssignment)
            # .filter(ProjectAssignment.project_id == project_id)
            # .filter(User.deleted_at.is_(None))
            # # .options(
            #     # load_only(User.id, User.name, User.role),
            #     # joinedload(User.project_assignment).load_only(ProjectAssignment.id)
            # # )
            # .first())
            # return u.project_assignment
            # return select(User).options(lazyload(User.project_assignment))
            return{
                "project":( 
                    Project()
                    .table()
                    .join(ProjectAssignment)
                    .filter(ProjectAssignment.user_id == user.id)
                    .filter(Project.id == project_id)
                    .filter(Project.deleted_at.is_(None))
                    .first()
                ),
                "users_dropdown": (
                    User().table()
                    .join(ProjectAssignment)
                    .filter(ProjectAssignment.project_id == project_id)
                    .filter(User.deleted_at.is_(None))
                    .options(
                        load_only(User.id, User.name, User.role),
                        # joinedload(User.project_assignments).load_only(ProjectAssignment.id)
                    )
                    .all()
                )
            }
    
    