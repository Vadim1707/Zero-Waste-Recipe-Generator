import uvicorn
from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
from uuid import uuid4, UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("6b4dbab4-b529-40bf-acfc-89b35a111783"), 
        first_name="Rada",
        middle_name="Poraieva",
        gender = Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("5632753b-d5d2-4aa6-9c7d-44e7a272b146"), 
        first_name="Alex",
        middle_name="Poraiev",
        gender = Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Woofer"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
