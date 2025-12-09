from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import users

app = FastAPI(title="CloudTech Backend")

# Allow frontend to access backend
origins = [
    "http://localhost:3000",            # local frontend
    "https://your-frontend.vercel.app"  # deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your users router with /api prefix
app.include_router(users.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "CloudTech API is running"}
