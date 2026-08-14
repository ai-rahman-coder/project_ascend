from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):

    token = credentials.credentials
    
    if token == "user_1":
        return "user_1"

    if token == "user_2":
        return "user_2"

    raise HTTPException(
        status_code=401,
        detail="Invalid authentication credentials"
    )