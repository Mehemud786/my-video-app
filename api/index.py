from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Python Video Call App")

# Enable CORS for safety
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RoomRequest(BaseModel):
    room_id: str

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "message": "Backend is running on Vercel"}

@app.post("/api/room")
def create_room(data: RoomRequest):
    return {"room_id": data.room_id, "status": "active"}