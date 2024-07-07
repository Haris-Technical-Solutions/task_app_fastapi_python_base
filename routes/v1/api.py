from fastapi import FastAPI, Depends, Request
from App.Http.Controllers.Home import Home
from App.Http.Controllers.Auth import Auth
from App.Http.Controllers.Profile import Profile
# from App.Http.Controllers.Auth import Auth
from typing import Callable
from App.Http.Middlewares.Middleware import Middleware
import time



API_VERSION = '/v1'



class api:
    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_middleware()
        self.setup_routes()

    def setup_middleware(self):
        self.app.middleware("http")(Middleware().boot)
        # return self.app
        # await self.app.add_middleware(Middleware().boot)

    def setup_routes(self):
        self.app.get(f"{API_VERSION}/")(Home().index)
        # self.app.get(f"{API_VERSION}/store")(Home().store)

        # Auth-----------------------------------------------------------------------------------------
        self.app.post(f"{API_VERSION}/login")(Auth().login)
        self.app.post(f"{API_VERSION}/register")(Auth().register)
        self.app.post(f"{API_VERSION}/auth/user")(Auth().user)
        # Profile-----------------------------------------------------------------------------------------
        self.app.post(f"{API_VERSION}/profile")(Profile().profile)

        # self.app.get(f"{API_VERSION}/users/me/", response_model=User)(Auth().login_for_access_token)
        # self.app.get(f"{API_VERSION}/users/me/items/")(Auth().read_own_items)

        # self.app.post(f"{API_VERSION}/token")(Auth().login_for_access_token)
        # self.app.get(f"{API_VERSION}/users/me")(Auth().read_users_me)
        # self.app.get(f"{API_VERSION}/users/me/items")(Auth().read_own_items)
        