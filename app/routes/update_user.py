from fastapi import APIRouter, HTTPException
from app.models import User
from app.db import db

router = APIRouter()

@router.patch("/users/{phone}")
def update_user(phone: str, user: User):
    if phone not in db:
        raise HTTPException(status_code=404, detail="User not found.")
    db[phone] = user.name
    return {"message": "User updated successfully."}
