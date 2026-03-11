from fastapi import APIRouter

router = APIRouter()

# temporary users
USER_DB = {
    "student1": "1234"
}


@router.post("/login")
async def login(data: dict):

    username = data.get("username")
    password = data.get("password")

    if username in USER_DB and USER_DB[username] == password:
        return {"status": "success"}

    return {"status": "invalid"}