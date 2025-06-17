from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from .jwt_handler import decode_access_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            try:
                payload = decode_access_token(credentials.credentials)
                return payload
            except JWTError:
                raise HTTPException(status_code=403, detail="Invalid or expired token.")
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization header.")

 