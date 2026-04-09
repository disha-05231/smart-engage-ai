import uvicorn
import threading
from app.services.event_engine import monitor_cart

if __name__ == "__main__":
    
    # Start background thread
    thread = threading.Thread(target=monitor_cart, daemon=True)
    thread.start()

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)