import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/room")
def create_room():
    # Generate a random 4-digit ID as a string
    room_id = str(random.randint(1000, 9999))
    return {"roomId": room_id}