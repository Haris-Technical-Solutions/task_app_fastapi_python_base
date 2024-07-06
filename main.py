# from typing import Union
from fastapi import FastAPI
from routes.v1.api import api

app = FastAPI()

# load api routes
api(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# fastapi dev main.py
