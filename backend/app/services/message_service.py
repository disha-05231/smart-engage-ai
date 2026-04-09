from app.db.mock_db import users, carts, analytics
from app.services.ai_engine import generate_smart_message, recommend_product
from app.services.consent_service import has_consent
from app.integrations.whatsapp_api import send_whatsapp
from app.integrations.sms_api import send_sms

def create_message(user_id):
    
    user = users.get(user_id)
    cart_items = carts.get(user_id)

    if not user or not cart_items or not has_consent(user_id):
        return None

    message = generate_smart_message(user.name, cart_items)
    recommendations = recommend_product(cart_items)

    # ✅ SEND MESSAGES (IMPORTANT)
    send_whatsapp(user.phone, message)
    send_sms(user.phone, message)

    # ✅ Track analytics
    analytics["messages_sent"] += 1

    return {
        "user": user.name,
        "message": message,
        "recommended_products": recommendations
    }