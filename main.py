from typing import List
from pydantic import BaseModel
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("a06643dc-4486-406f-8d6e-e25f20d1259f"),
        first_name="Ahmad",
        last_name="Maulana",
        gender=Gender.male,
        roles=[Role.validator]
    ),
    User(
        id=UUID("73e0ebcb-e9a8-42c6-8047-ef396142ddfb"),
        first_name="Irfan",
        last_name="Nurmawan",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello" : "POIN"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def get_user(user:User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
