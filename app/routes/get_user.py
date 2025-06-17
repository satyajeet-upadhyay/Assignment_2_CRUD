from fastapi import APIRouter
from app.db import db

router = APIRouter()

@router.get("/users")
def get_user():
    return [{"name": name, "phone": phone} for phone, name in db.items()]
