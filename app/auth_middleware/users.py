from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel
from .jwt_handler import create_access_token

router = APIRouter()
password = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = {}

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(user: UserLogin):
    if user.username in db:
        raise HTTPException(status_code=400, detail="Username already exists.")
    hashed_password = password.hash(user.password)
    db[user.username] = hashed_password
    return {"message": "User created successfully."}

@router.post("/login")
def login(user: UserLogin):
    if user.username not in db:
        raise HTTPException(status_code=400, detail="Invalid username or password.")
    hashed_password = db[user.username]
    if not password.verify(user.password, hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password.")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
