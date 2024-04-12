from fastapi import FastAPI
from typing import List, Optional
from uuid import uuid4, UUID
import asyncio
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        #id=uuid4(),
        id = UUID('7e9e6f30-a302-465e-b902-fca864c9990a'),
        first_name="Naruto",
        last_name="Uzumaki",
        gender=Gender.male,
        roles=[Role.hokage]
    ),
    User(
            #id=uuid4(),
            id = UUID("f9bcfbc3-07be-4333-adbd-c35e18ab4634"),
            first_name="Himawari",
            last_name="Uzumaki",
            gender=Gender.female,
            roles=[Role.student, Role.user]
        )
]


@app.get("/")
async def root():
    return {'Hello': 'world'}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {'id': user.id}

print("nananananana")



