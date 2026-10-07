from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Python Video Call App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms: Dict[str, Dict[str, Any]] = {}

class SignalPayload(BaseModel):
    room_id: str
    type: str  # "offer", "answer", or "candidate"
    data: dict

@app.post("/api/signal")
def post_signal(payload: SignalPayload):
    if payload.room_id not in rooms:
        rooms[payload.room_id] = {"offer": None, "answer": None, "candidates": []}

    if payload.type == "offer":
        rooms[payload.room_id]["offer"] = payload.data
    elif payload.type == "answer":
        rooms[payload.room_id]["answer"] = payload.data
    elif payload.type == "candidate":
        rooms[payload.room_id]["candidates"].append(payload.data)

    return {"status": "success"}

@app.get("/api/signal/{room_id}")
def get_signal(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    return rooms[room_id]

@app.delete("/api/signal/{room_id}")
def clear_signal(room_id: str):
    if room_id in rooms:
        del rooms[room_id]
    return {"status": "cleared"}