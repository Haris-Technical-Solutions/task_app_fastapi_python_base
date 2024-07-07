# from typing import Union
from fastapi import FastAPI, Request
from routes.v1.api import api
import time

app = FastAPI()

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     # Extract the endpoint name from the request scope
#     endpoint = request.scope.get("endpoint", "Unknown endpoint")

#     # Get the class and function name from the endpoint
#     try:
#         class_name = endpoint.__self__.__class__.__name__  # Get class name
#         function_name = endpoint.__name__  # Get function name
#     except AttributeError:
#         class_name = "UnknownClass"
#         function_name = "UnknownFunction"

#     # Log information about the request and response
#     print(f"Request path: {request.url.path}")
#     print(f"Request method: {request.method}")
#     print(f"Target class: {class_name}")
#     print(f"Target function: {function_name}")
#     print(f"Target function: {endpoint}")  # This will print the target function name
#     print(f"Response status code: {response.status_code}")
#     print(f"Process time: {process_time} seconds")

#     response.headers["X-Process-Time"] = str(process_time)
#     return response


# load api routes
api(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# fastapi dev main.py
