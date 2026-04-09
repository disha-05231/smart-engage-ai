import random

# Simple product similarity (can upgrade later)
product_map = {
    "shoes": ["socks", "t-shirt"],
    "laptop": ["mouse", "keyboard"],
    "phone": ["earphones", "cover"],
    "t-shirt": ["jeans", "jacket"]
}

def recommend_product(cart_items):
    recommendations = []

    for item in cart_items:
        if item in product_map:
            recommendations.extend(product_map[item])

    return list(set(recommendations))


def generate_smart_message(user_name, cart_items):
    templates = [
        f"🔥 Hey {user_name}, your items {cart_items} are waiting! Checkout now!",
        f"🛒 {user_name}, don’t miss out on {cart_items}. Complete your purchase today!",
        f"💸 Special offer on {cart_items}, {user_name}! Grab them before they’re gone!"
    ]

    return random.choice(templates)