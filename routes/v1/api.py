from App.Http.Middlewares.Middleware import Middleware
from fastapi import FastAPI, Depends, Request
# from typing import Callable
# import time


from App.Http.Controllers.Home import Home
from App.Http.Controllers.Auth import Auth
from App.Http.Controllers.Profile import Profile
from App.Http.Controllers.Users import Users
from TaskApp.App.Http.Controllers.AdminProjects import AdminProjects
from TaskApp.App.Http.Controllers.Projects import Projects
from TaskApp.App.Http.Controllers.Tasks import Tasks
from TaskApp.App.Http.Controllers.TaskComments import TaskComments


API_VERSION = '/v1'

class api:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_middleware()
        self.setup_routes()

    def setup_middleware(self):
        self.app.middleware("http")(Middleware().boot)

    def setup_routes(self):
        self.app.get(f"{API_VERSION}/")(Home().index)
        # self.app.get(f"{API_VERSION}/store")(Home().store)

        # Auth-------------------------------------------------------------------------------------------
        self.app.post(f"{API_VERSION}/login")(Auth().login)
        self.app.post(f"{API_VERSION}/register")(Auth().register)
        # self.app.post(f"{API_VERSION}/auth/user")(Auth().user)
        # Profile-----------------------------------------------------------------------------------------
        self.app.get(f"{API_VERSION}/profile")(Profile().index)
        self.app.post(f"{API_VERSION}/profile/update")(Profile().update)
        # Users-------------------------------------------------------------------------------------------
        self.app.get(f"{API_VERSION}/admin/user")(Users().index)
        self.app.post(f"{API_VERSION}/admin/user")(Users().store)
        self.app.put(f"{API_VERSION}/admin/user/{{user_id}}")(Users().update)
        self.app.delete(f"{API_VERSION}/admin/user")(Users().delete)
        # AdminProjects-----------------------------------------------------------------------------------
        self.app.get(f"{API_VERSION}/admin/project")(AdminProjects().index)
        self.app.post(f"{API_VERSION}/admin/project")(AdminProjects().store)
        self.app.put(f"{API_VERSION}/admin/project/{{project_id}}")(AdminProjects().update)
        self.app.delete(f"{API_VERSION}/admin/project")(AdminProjects().delete)

        self.app.post(f"{API_VERSION}/admin/project/{{project_id}}/assign")(AdminProjects().assign)
        # Projects-----------------------------------------------------------------------------------------
        self.app.get(f"{API_VERSION}/project")(Projects().index)
        self.app.get(f"{API_VERSION}/project/{{project_id}}")(Projects().show)
        # Tasks--------------------------------------------------------------------------------------------
        self.app.get(f"{API_VERSION}/project/{{project_id}}/task")(Tasks().index)
        self.app.post(f"{API_VERSION}/project/{{project_id}}/task")(Tasks().store)
        self.app.put(f"{API_VERSION}/project/{{project_id}}/task/{{task_id}}")(Tasks().update)
        self.app.delete(f"{API_VERSION}/project/{{project_id}}/task")(Tasks().delete)

        # self.app.post(f"{API_VERSION}/admin/project/{{project_id}}/task/{{task_id}}/assign")(AdminProjects().assign)
        
        # TaskComments--------------------------------------------------------------------------------------------
        self.app.get(f"{API_VERSION}/project/{{project_id}}/task/{{task_id}}/comment")(TaskComments().index)
        self.app.post(f"{API_VERSION}/project/{{project_id}}/task/{{task_id}}/comment")(TaskComments().store)
        self.app.put(f"{API_VERSION}/project/{{project_id}}/task/{{task_id}}/comment/{{comment_id}}")(TaskComments().update)
        self.app.delete(f"{API_VERSION}/project/{{project_id}}/task/{{task_id}}/comment/{{comment_id}}")(TaskComments().delete)










        # self.app.get(f"{API_VERSION}/users/me/", response_model=User)(Auth().login_for_access_token)
        # self.app.get(f"{API_VERSION}/users/me/items/")(Auth().read_own_items)

        # self.app.post(f"{API_VERSION}/token")(Auth().login_for_access_token)
        # self.app.get(f"{API_VERSION}/users/me")(Auth().read_users_me)
        # self.app.get(f"{API_VERSION}/users/me/items")(Auth().read_own_items)
        