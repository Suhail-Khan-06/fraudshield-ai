from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FraudShield AI",
    version="1.0.0",
    description="Intelligent Financial Fraud Detection Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "FraudShield AI API is running",
        "version": "1.0.0",
        "status": "healthy"
    }