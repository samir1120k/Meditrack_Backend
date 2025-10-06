from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.patients import router as patients_router

app = FastAPI(title="Patient Management API")

# More explicit CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://samir1120k.github.io",
    "*"  # Fallback for all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Include patient routes
app.include_router(patients_router, prefix="/patients", tags=["Patients"])

@app.get("/")
def root():
    return {"message": "Patient Management API is running"}