from collections import Counter
from io import BytesIO

import pandas as pd

from backend.services.model_loader import model_loader
from backend.services.prediction_service import predict_transaction


def analyze_csv(file_bytes: bytes) -> dict:
    """
    Analyze all transactions in an uploaded CSV file.
    Returns row-level predictions and aggregate summary statistics.
    """

    # Read CSV from uploaded bytes
    df = pd.read_csv(BytesIO(file_bytes))

    # Ensure required columns are present
    missing_columns = set(model_loader.feature_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    # Keep only the required columns and preserve order
    df = df[model_loader.feature_columns]

    results = []

    # Predict each row
    for _, row in df.iterrows():
        transaction = row.to_dict()
        prediction = predict_transaction(transaction)
        results.append(prediction)

    # Aggregate statistics
    total_transactions = len(results)
    fraud_predictions = sum(
        1 for result in results if result["is_fraud"]
    )

    average_risk_score = round(
        sum(result["risk_score"] for result in results)
        / total_transactions,
        2,
    ) if total_transactions > 0 else 0.0

    severity_distribution = dict(
        Counter(result["severity"] for result in results)
    )

    return {
        "total_transactions": total_transactions,
        "fraud_predictions": fraud_predictions,
        "average_risk_score": average_risk_score,
        "severity_distribution": severity_distribution,
        "results": results,
    }