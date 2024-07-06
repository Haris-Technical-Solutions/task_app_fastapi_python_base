from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi.responses import JSONResponse

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# async def log_request(request: Request):
#     print(f"Request: {request.method} {request.url}")

# async def check_authentication(token: Annotated[str, Depends(oauth2_scheme)]):
#     if token != "fake-super-secret-token":
#         raise HTTPException(status_code=401, detail="Invalid token")

class AuthCheck:
    # async def __call__(self, request: Request, call_next):
    #     return 'hello'
    #     # Perform your authentication checks here
    #     if not request.headers.get("Authorization"):
    #         return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
        
    #     # If authentication is successful, proceed to the next middleware or route
    #     response = await call_next(request)
    #     return response
    
    async def boot(self, request: Request):
        pass
        # raise HTTPException(status_code=200, detail=await request.json())
        # try:
        #     body = await request.json()
        #     token = body.get('token')
        #     if not token:
        #         raise HTTPException(status_code=401, detail="Token not found")
        #     # You can perform further validation or processing here
        #     # For example, decode the token and verify it
        #     return {"token": token}  # Return the token or additional data if needed
        # except Exception as e:
        #     raise HTTPException(status_code=401, detail=str(e))
