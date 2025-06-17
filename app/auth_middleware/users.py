from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel
from .jwt_handler import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# For simplicity → in-memory user "database"
fake_users_db = {}

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(user: UserLogin):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists.")
    hashed_password = pwd_context.hash(user.password)
    fake_users_db[user.username] = hashed_password
    return {"message": "User created successfully."}

@router.post("/login")
def login(user: UserLogin):
    if user.username not in fake_users_db:
        raise HTTPException(status_code=400, detail="Invalid username or password.")
    hashed_password = fake_users_db[user.username]
    if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password.")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
