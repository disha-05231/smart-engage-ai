from pydantic import BaseModel
from typing import List

class Cart(BaseModel):
    user_id: str
    items: List[str]