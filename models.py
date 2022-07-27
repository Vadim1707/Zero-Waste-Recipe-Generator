from typing import Optional, List, Dict
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

class Recipe(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    ingredients: List[str]
    description: str

    #TODO ingredients: Dict[str, str] ingredient - amount, etc.
