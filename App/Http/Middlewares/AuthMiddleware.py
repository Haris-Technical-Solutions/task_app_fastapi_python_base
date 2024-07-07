from fastapi import Request
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider
from fastapi import HTTPException, Depends, status
# from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware():
    def __init__(self):
        print('from auth middleware')
    def __call__(self, request: Request, call_next, response):
        print('from auth middleware call')
        self.boot(request, call_next, response)
    
    def boot(self, request: Request, call_next, response):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")

        print(token)
        if not token:
            raise HTTPException(status_code=401, detail="Token Missing")
            
        if token:
            user = AuthServiceProvider().get_current_user(token)
            response.headers["X-User-id"] = str(user.id)