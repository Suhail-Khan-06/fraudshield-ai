from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.v1.routes_predict import router as predict_router
from backend.api.v1.routes_report import router as report_router
from backend.api.v1.routes_batch import router as batch_router

app = FastAPI(
    title="FraudShield AI",
    version="1.0.0",
    description="Intelligent Financial Fraud Detection Platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prediction API
app.include_router(
    predict_router,
    prefix="/api/v1",
    tags=["Prediction"],
)

# PDF Report API
app.include_router(
    report_router,
    prefix="/api/v1",
    tags=["Reports"],
)

app.include_router(
    batch_router,
    prefix="/api/v1",
    tags=["Batch Analysis"],
)


@app.get("/")
def root():
    return {
        "message": "FraudShield AI API is running",
        "version": "1.0.0",
        "status": "healthy",
    }