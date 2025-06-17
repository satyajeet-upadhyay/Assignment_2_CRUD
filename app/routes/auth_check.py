from fastapi import APIRouter, Depends
from ..auth_middleware.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/secure-endpoint", dependencies=[Depends(JWTBearer())])
def secure_data():
    return {"message": "This is a protected endpoint!"}
 