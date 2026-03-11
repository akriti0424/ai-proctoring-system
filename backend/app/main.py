from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
import base64
import cv2
import numpy as np

from app.controllers import exam_controller
from app.controllers import auth_controller
from app.websocket_manager import manager

# A very basic dummy implementation of face detection if it fails to import
try:
    from app.services.face_detection import detect
except:
    def detect(frame): return []

app = FastAPI()

# project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# serve static files
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

# include APIs
app.include_router(auth_controller.router, prefix="/api")
app.include_router(exam_controller.router, prefix="/api")


@app.get("/")
def login_page():
    return FileResponse(FRONTEND_DIR / "pages/login.html")

@app.get("/login")
def explicit_login_page():
    return FileResponse(FRONTEND_DIR / "pages/login.html")


@app.get("/exam")
def exam_page():
    return FileResponse(FRONTEND_DIR / "pages/exam.html")


@app.get("/admin")
def admin_page():
    return FileResponse(FRONTEND_DIR / "pages/admin.html")

# ==================== WEBSOCKETS ====================

@app.websocket("/ws/admin/stream")
async def websocket_admin_endpoint(websocket: WebSocket):
    await manager.connect_admin(websocket)
    try:
        while True:
            # Just keep the connection alive
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect_admin(websocket)

@app.websocket("/ws/exam/stream")
async def websocket_exam_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            
            if data.get("type") == "frame":
                # Forward to admin dashboard
                await manager.broadcast_to_admins({
                    "type": "frame",
                    "image": data["image"]
                })
                
                # Run Face Detection
                encoded_data = data["image"].split(',')[1]
                nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
                frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                faces = detect(frame)
                
                msg = None
                if len(faces) == 0:
                    msg = "No Face Detected from Student!"
                elif len(faces) > 1:
                    msg = "Multiple Faces! Possible Cheating."
                
                if msg:
                    await manager.broadcast_to_admins({"type": "violation", "message": msg})
                    await websocket.send_json({"type": "violation", "message": msg})
                    
            elif data.get("type") == "violation":
                v_type = data.get("violation_type")
                if v_type == "tab_switch":
                    await manager.broadcast_to_admins({
                        "type": "violation", 
                        "message": "Student switched tabs!"
                    })

    except WebSocketDisconnect:
        pass
