from fastapi import FastAPI, Depends
from App.v1.Controllers.Home import Home
from App.v1.Controllers.Auth import Auth

from App.v1.Middlewares.AuthCheck import AuthCheck



API_VERSION = '/v1'

class api:
    # def __init__(self,app:FastAPI, db):
    #     app.get(API_VERSION)(Home.index)

    def __init__(self, app: FastAPI):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        self.app.get(f"{API_VERSION}/")(Home().index)
        # self.app.get(f"{API_VERSION}/store")(Home().store)
        # Auth
        self.app.post(f"{API_VERSION}/login")(Auth().login)
        self.app.post(f"{API_VERSION}/register")(Auth().register)
        self.app.post(f"{API_VERSION}/auth/user", dependencies=[Depends(AuthCheck().boot)])(Auth().user)

        # self.app.get(f"{API_VERSION}/users/me/", response_model=User)(Auth().login_for_access_token)
        # self.app.get(f"{API_VERSION}/users/me/items/")(Auth().read_own_items)

        # self.app.post(f"{API_VERSION}/token")(Auth().login_for_access_token)
        # self.app.get(f"{API_VERSION}/users/me")(Auth().read_users_me)
        # self.app.get(f"{API_VERSION}/users/me/items")(Auth().read_own_items)
        