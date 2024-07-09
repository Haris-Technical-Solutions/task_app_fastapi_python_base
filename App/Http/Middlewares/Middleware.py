from fastapi import Request, HTTPException, Depends, status
# from fastapi.security import OAuth2PasswordBearer
# from typing import Annotated
from fastapi.responses import JSONResponse
import time
import numpy as np
from App.Http.Middlewares.AuthMiddleware import AuthMiddleware
from TaskApp.App.Http.Middlewares.AdminCheckMiddleware import AdminCheckMiddleware



class Middleware:
    def __init__(self):
        self.middlewares = {
            "AuthMiddleware" : [
                "Profile.*",
                "Users.*",
                "Projects.*"

            ],
            "AdminCheckMiddleware" : [
                "Users.*",
                "AdminProjects.*"
            ]
        }


    def load_middlewares(self, class_name, function_name):
        included = []
        for middleware, targets in self.middlewares.items():
            if class_name+'.*' in targets:
                included.append(middleware)
            elif class_name+'.'+function_name in targets:
                included.append(middleware)

        self.register_middleware(included)

    def instantiate_class(self, class_name):
        # Get the class from the global namespace
        class_ = globals()[class_name]
        # Instantiate the Middleware
        instance = class_()
        instance(self.request, self.call_next, self.response)
    
    def register_middleware(self, middlewares):
        print(f"included Boot: ----------------------------------------")
        for middleware in middlewares:
            self.instantiate_class(middleware)




    async def boot(self, request: Request, call_next):
        self.request = request
        self.call_next = call_next

        start_time = time.time()

        response = await call_next(request)
        self.response = response
        # try:
        #     response = await call_next(request)
        # except HTTPException as exc:
        #     # Handle HTTP exceptions raised by middleware or routes
        #     response = exc
        # except Exception as exc:
        #     # Handle other exceptions (e.g., internal server errors)
        #     response = HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
        # self.response = response

        process_time = time.time() - start_time
        # Extract the endpoint name from the request scope
        endpoint = request.scope.get("endpoint", "Unknown endpoint")

        # Get the class and function name from the endpoint
        try:
            class_name = endpoint.__self__.__class__.__name__  # Get class name
            function_name = endpoint.__name__  # Get function name
        except AttributeError:
            class_name = "UnknownClass"
            function_name = "UnknownFunction"

        try:

            self.load_middlewares(class_name, function_name)
            # raise HTTPException(status_code=401, detail="Invalid token")

        except HTTPException as http_exc:
            # Catch specific HTTPExceptions and return them directly
            return JSONResponse(
                status_code=http_exc.status_code,
                content={"detail": http_exc.detail}
            )

        # raise HTTPException(status_code=401, detail="Invalid token")
        # Log information about the request and response
        print(f"Middleware Boot: ----------------------------------------")
        # print(f"Request path: {request.url.path}")
        # print(f"Request method: {request.method}")
        # print(f"Target class: {class_name}")
        # print(f"Target function: {function_name}")
        # print(f"Target function: {endpoint}")  # This will print the target function name
        # print(f"Response status code: {response.status_code}")
        # print(f"Process time: {process_time} seconds")
        

        response.headers["X-Process-Time"] = str(process_time)
        return response
