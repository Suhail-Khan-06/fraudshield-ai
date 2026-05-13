def get_severity(risk_score: int) -> str:
    if risk_score < 25:
        return "Low"
    elif risk_score < 50:
        return "Medium"
    elif risk_score < 75:
        return "High"
    return "Critical"


def get_recommendations(severity: str) -> list[str]:
    recommendations = {
        "Low": [
            "Approve transaction.",
            "Continue routine monitoring.",
        ],
        "Medium": [
            "Flag for secondary review.",
            "Request additional verification.",
        ],
        "High": [
            "Temporarily hold transaction.",
            "Contact customer for confirmation.",
        ],
        "Critical": [
            "Block transaction immediately.",
            "Escalate to fraud investigation team.",
            "Freeze account pending review.",
        ],
    }
    return recommendations[severity]


def calculate_risk_score(
    fraud_probability: float,
    anomaly_score: float,
) -> dict:
    """
    Combine supervised and anomaly signals.

    fraud_probability: 0 to 1
    anomaly_score: 0 to 1 (higher = more anomalous)
    """

    combined_score = (
        fraud_probability * 0.80 +
        anomaly_score * 0.20
    )

    risk_score = min(100, max(0, round(combined_score * 100)))
    severity = get_severity(risk_score)

    return {
        "risk_score": risk_score,
        "severity": severity,
        "recommendations": get_recommendations(severity),
    }