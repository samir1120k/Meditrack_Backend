from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.patients import router as patients_router

app = FastAPI(title="Patient Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include patient routes
app.include_router(patients_router, prefix="/patients", tags=["Patients"])

@app.get("/")
def root():
    return {"message": "Patient Management API is running"}
