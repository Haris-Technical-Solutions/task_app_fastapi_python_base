from App.Http.Controllers.Controller import Controller
from fastapi import Depends, Form, Security
from App.Http.RequestForms.Auth import Token
from App.Http.RequestForms.User import ProfileForm
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider

from App.Http.Models.Project import Project
from App.Http.Models.ProjectAssignment import ProjectAssignment
from App.Http.Controllers.Auth import Auth

from datetime import datetime

from sqlalchemy import update

from TaskApp.App.Http.RequestForms.Projects import UpdateForm, StoreForm, AssignUsersForm

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
    
    