import uuid
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
    # Generate a unique room/call ID
    room_id = str(uuid.uuid4())[:8]
    return {"roomId": room_id}