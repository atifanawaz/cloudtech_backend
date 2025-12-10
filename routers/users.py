#users.py
from fastapi import APIRouter
from models import UserData
from database import db

router = APIRouter()

@router.post("/submit")
def submit_data(user_data: UserData):
    result = db.users.insert_one(user_data.dict())
    return {"message": "Data submitted successfully", "id": str(result.inserted_id)}

@router.get("/all")
def get_all_data():
    data = list(db.users.find({}, {"_id": 0}))
    return {"users_data": data}

