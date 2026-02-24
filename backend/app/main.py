from fastapi import FastAPI

app = FastAPI(title = "AI Proctoring System")

@app.get("/")
def root():
    return{"message": "Backend running successfully"}