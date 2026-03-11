from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.auth_controller import router as auth_router
from app.controllers.exam_controller import router as exam_router
from app.controllers.admin_controller import router as admin_router

app = FastAPI(title="AI Proctoring System")

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include controllers
app.include_router(auth_router)
app.include_router(exam_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return {"message": "AI Proctoring System Running"}