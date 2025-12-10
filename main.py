from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import users

app = FastAPI(title="CloudTech Backend")

origins = [
    "http://localhost:3000",           # for local testing
    "https://cloudtech-frontend-final.vercel.app"  # frontend deployed URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/api")
