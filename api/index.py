from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI(title="Python Video Call App")

class RoomRequest(BaseModel):
    room_id: str

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "message": "Backend is running on Vercel"}

@app.post("/api/room")
def create_room(data: RoomRequest):
    # Here you could integrate with token generators (e.g., Daily, Agora, Twilio)
    return {"room_id": data.room_id, "status": "active"}

# Mount public directory for frontend static assets if needed
# Vercel routes static files automatically if placed in public/