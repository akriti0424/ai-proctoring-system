import os
import shutil
from fastapi import UploadFile

# Use absolute path to the backend/recordings directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RECORDINGS_DIR = os.path.join(BASE_DIR, "recordings")

def save_recording(file: UploadFile) -> str:
    # Ensure directory exists
    os.makedirs(RECORDINGS_DIR, exist_ok=True)
    
    file_location = os.path.join(RECORDINGS_DIR, file.filename)
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return file_location
