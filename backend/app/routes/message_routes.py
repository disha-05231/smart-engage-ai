from fastapi import APIRouter
from app.services.message_service import create_message

router = APIRouter()

@router.get("/send/{user_id}")
def send_message(user_id: str):
    
    result = create_message(user_id)

    if not result:
        return {"error": "No data found for user"}

    return {
        "status": "message generated",
        "data": result
    }