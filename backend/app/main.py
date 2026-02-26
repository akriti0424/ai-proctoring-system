from fastapi import FastAPI
from app.webcam_service import WebcamService
from app.face_detection import detect_faces

app = FastAPI(title="Basic Proctoring")

webcam = WebcamService()
last_status = "Not started"

def analyze(frame):
    global last_status
    faces = detect_faces(frame)

    if faces == 0:
        last_status = "No face detected"
    elif faces > 1:
        last_status = "Multiple faces detected"
    else:
        last_status = "Single face detected"

@app.get("/start-proctoring")
def start_proctoring():
    webcam.start(analyze)
    return {"status": "Proctoring started"}

@app.get("/status")
def get_status():
    return {"status": last_status}

@app.get("/stop-proctoring")
def stop_proctoring():
    webcam.stop()
    return {"status": "Proctoring stopped, video saved"}