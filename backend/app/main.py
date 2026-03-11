from fastapi import FastAPI
from fastapi.staticifiles import StaticFiles
from fastapi.responses import FileResponse


#importing controllers
from app.controllers.exam_controller import router as exam_router
from app.controllers.auth_controller import router as auth_router
from app.controllers.admin_controller import router as admin_router

app = FastAPI(title="AI Proctoring System")


#including API routers
app.include_router(auth_router)
app.include_router(exam_router)
app.include_router(admin_router)


#Serving fontend static files
app.mount("/static", StaticFiles(directory = "../frontend"), name = "static")

@app.get("/")
def home():
    return FileResponse("../frontend/pages/login.html")
