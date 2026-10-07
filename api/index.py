from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Python Room Video Call App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory transient store for room exchange states
rooms: Dict[str, Dict[str, Any]] = {}

class SignalingPayload(BaseModel):
    room_id: str
    data: dict

@app.post("/api/signal/set")
def set_signal(payload: SignalingPayload):
    rooms[payload.room_id] = payload.data
    return {"status": "success", "room_id": payload.room_id}

@app.get("/api/signal/get/{room_id}")
def get_signal(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found or empty")
    return {"room_id": room_id, "data": rooms[room_id]}

@app.delete("/api/signal/clear/{room_id}")
def clear_signal(room_id: str):
    if room_id in rooms:
        del rooms[room_id]
    return {"status": "cleared"}