from fastapi import APIRouter

from backend.api.schemas.prediction import (
    PredictionRequest,
    PredictionResponse,
)
from backend.services.prediction_service import predict_transaction

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    result = predict_transaction(request.model_dump())
    return result