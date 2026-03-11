from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter(prefix="/auth", tags=["Auth"])

# Temporary session storage
sessions = {}

class LoginRequest(BaseModel):
    name: str
    email: str


@router.post("/login")
def login(data: LoginRequest):

    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "name": data.name,
        "email": data.email,
        "status": "exam_not_started"
    }

    return {
        "message": "Login successful",
        "session_id": session_id
    }
