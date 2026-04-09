from fastapi import FastAPI
from app.routes import user_routes, cart_routes, message_routes
from app.routes import analytics_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartEngage AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/user")
app.include_router(cart_routes.router, prefix="/cart")
app.include_router(message_routes.router, prefix="/message")
app.include_router(analytics_routes.router, prefix="/analytics")

@app.get("/")
def home():
    return {"message": "SmartEngage AI Backend Running 🚀"}