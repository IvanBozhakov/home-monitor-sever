from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer
import os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("API_BEARER_TOKEN")

security_scheme = HTTPBearer()

def verify_token(authorization: dict = Depends(security_scheme)):
    token = authorization.credentials
    if token != BEARER_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token