from fastapi import APIRouter, HTTPException
from app.models import User
from app.db import db

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    if user.phone in db:
        raise HTTPException(status_code=400, detail="Phone number already exists.")
    db[user.phone] = user.name
    return {"message": "User created successfully."}

 