import time
from app.db.mock_db import carts
from app.services.message_service import create_message

def monitor_cart():
    print("📡 Monitoring cart activity...")

    while True:
        for user_id in carts:
            result = create_message(user_id)
            if result:
                print(f"📩 Auto message for {user_id}: {result['message']}")
        
        time.sleep(10)