# Updated for CORS support
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import users

app = FastAPI(title="CloudTech Backend")

origins = [
    "http://localhost:3000",
    "https://your-frontend.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "CloudTech API is running"}
