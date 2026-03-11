from fastapi import APIRouter
from app.monitoring.violation_detector import handle_violation

router = APIRouter()

@router.post("/violation")
async def receive_violation(data: dict):

    violation_type = data.get("type")

    result = handle_violation(violation_type)

    return result
from fastapi import UploadFile, File
from app.services.recording_service import save_recording

@router.post("/upload_recording")
async def upload_recording(file: UploadFile = File(...)):
    # Save the file using the recording service
    file_path = save_recording(file)
    return {"message": "Recording uploaded successfully", "path": file_path}
