from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/room-token")
def create_room():
    # Here you would typically integrate with a video provider SDK 
    # (e.g., Daily.co, Agora, or LiveKit) to generate secure room URLs or tokens.
    room_id = "sample-room-123"
    return {"room_id": room_id, "status": "ready"}