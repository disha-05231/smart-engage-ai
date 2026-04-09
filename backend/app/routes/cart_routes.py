from fastapi import APIRouter
from app.models.cart_model import Cart
from app.db.mock_db import carts

router = APIRouter()

@router.post("/cart")
def add_to_cart(cart: Cart):
    carts[cart.user_id] = cart.items
    return {"message": "Cart updated"}

@router.get("/cart/{user_id}")
def get_cart(user_id: str):
    return {"user_id": user_id, "items": carts.get(user_id, [])}