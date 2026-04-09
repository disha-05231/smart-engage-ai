from fastapi import APIRouter
from app.models.user_model import User
from app.db.mock_db import users, consent

router = APIRouter()

@router.post("/register")
def register_user(user: User):
    users[user.user_id] = user
    consent[user.user_id] = user.consent
    return {"message": "User registered successfully"}

@router.get("/users")
def get_users():
    return users