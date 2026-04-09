from fastapi import APIRouter
from app.db.mock_db import analytics

router = APIRouter()

@router.get("/")
def get_analytics():
    return analytics