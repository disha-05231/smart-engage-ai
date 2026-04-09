from app.db.mock_db import consent

def has_consent(user_id):
    return consent.get(user_id, False)

def opt_out(user_id):
    consent[user_id] = False
    return {"message": "User unsubscribed successfully"}