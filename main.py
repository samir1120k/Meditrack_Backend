from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.patients import router as patients_router

app = FastAPI(title="Patient Management API")

allowed_origins = [
    "https://satyam1120k.github.io",  # GitHub Pages origin (no path)
    "http://localhost:5173",         # Vite dev
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,          # keep True only with explicit origins
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patients_router, prefix="/patients", tags=["Patients"])

@app.get("/")
def root():
    return {"message": "Patient Management API is running"}