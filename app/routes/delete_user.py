from fastapi import APIRouter, HTTPException
from app.db import db

router = APIRouter()

@router.delete("/users/{phone}")
def delete_user(phone: str):
    if phone not in db:
        raise HTTPException(status_code=404, detail="User not found.")
    del db[phone]
    return {"message": "User deleted successfully."}
 