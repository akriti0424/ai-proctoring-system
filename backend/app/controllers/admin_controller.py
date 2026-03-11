from fastapi import APIRouter

router = APIRouter()

students = ["Akriti"]
violations = []
risk_score = 0


@router.get("/admin/data")
def admin_data():
    return {
        "students": students,
        "violations": violations,
        "risk_score": risk_score
    }