from fastapi import FastAPI
from routers import users

app = FastAPI(title="CloudTech Backend")

app.include_router(users.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "CloudTech API is running"}
