# ai-proctoring-system

## Objective

This project aims to build an AI-based online proctoring system that monitors candidates during online examinations.
The system detects suspicious behavior such as multiple faces, absence of face, tab switching, and later extends
to identity verification and deepfake detection.

## Tech Stack

- Backend: Python, FastAPI
- Server: Uvicorn
- Computer Vision: OpenCV
- Frontend: HTML, CSS, JavaScript
- Version Control: Git & GitHub

## System Architecture

Frontend (Browser)
↓
FastAPI Backend (Uvicorn Server)
↓
Webcam Frame Capture (OpenCV)
↓
Face Detection & Rule Engine
↓
Violation Logging & Risk Scoring

## Project Structure

ai-proctoring-system/
│
├── backend/
│ ├── app/
│ │ ├── main.py # FastAPI entry point
│ │ ├── face_detection.py # Face detection logic
│ │ ├── violation.py # Violation logging
│ │ └── risk_score.py # Risk calculation
│ └── requirements.txt
│
├── frontend/
│ ├── index.html # UI
│ ├── script.js # Webcam & tab detection
│ └── style.css
│
├── recordings/ # Exam recordings (future)
└── docs/ # Documentation

## MVP (Minimum Viable Product) Scope

✔ Backend server setup using FastAPI  
✔ Webcam access and live monitoring  
✔ Face detection (zero / single / multiple faces)  
✔ Tab-switch detection  
✔ Violation logging  
✔ Basic rule-based risk scoring

## How to Run the Project

### Backend

1. Clone the repository
2. Navigate to backend folder
3. Create and activate virtual environment
4. Install dependencies
5. Run the server

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Future Scope

- Identity verification using face matching
- Liveness detection (blink, head movement)
- Deepfake detection using CNN-based models
- Eye gaze tracking
- Audio-based cheating detection
- Admin dashboard for monitoring
