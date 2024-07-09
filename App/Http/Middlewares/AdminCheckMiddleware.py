from fastapi import Request
from fastapi import HTTPException, Depends, status
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider
from App.Http.Models.User import UserRoles

class AdminCheckMiddleware:
    def __init__(self):
        print('from role middleware')
    def __call__(self, request: Request, call_next, response):
        print('from role middleware call /////////////////////')
        self.boot(request, call_next, response)

    def boot(self, request: Request, call_next, response):
        # print(response.headers["X-User-role"])
        if(response.headers["X-User-role"] != "UserRoles.admin"):
            raise HTTPException(status_code=401, detail="You are not an Admin User")

        # token = request.headers.get("Authorization", "").replace("Bearer ", "")

        # # print(token)
        # if not token:
        #     raise HTTPException(status_code=401, detail="Token Missing")
            
        # if token:
        #     user = AuthServiceProvider().get_current_user(token)
        #     response.headers["X-User-id"] = str(user.id)