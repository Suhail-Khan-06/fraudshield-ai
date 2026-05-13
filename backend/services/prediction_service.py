import pandas as pd

from backend.services.explainability_service import get_top_risk_factors
from backend.services.model_loader import model_loader
from backend.services.risk_engine import calculate_risk_score


def predict_transaction(transaction: dict) -> dict:
    df = pd.DataFrame([transaction])
    df = df[model_loader.feature_columns]

    # Fraud probability
    fraud_probability = float(
        model_loader.xgb_model.predict_proba(df)[0][1]
    )

    # Anomaly score
    raw_score = float(model_loader.iso_model.score_samples(df)[0])
    anomaly_score = max(0.0, min(1.0, (-raw_score) / 0.5))

    # Risk scoring
    risk_info = calculate_risk_score(
        fraud_probability=fraud_probability,
        anomaly_score=anomaly_score,
    )

    # SHAP explanations
    key_risk_factors = get_top_risk_factors(df, top_n=5)

    return {
        "is_fraud": fraud_probability >= 0.5,
        "fraud_probability": round(fraud_probability, 6),
        "anomaly_score": round(anomaly_score, 6),
        "key_risk_factors": key_risk_factors,
        **risk_info,
    }