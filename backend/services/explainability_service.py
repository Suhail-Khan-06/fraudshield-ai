import pandas as pd
import shap

from backend.services.model_loader import model_loader

# Create SHAP explainer once at startup
explainer = shap.TreeExplainer(model_loader.xgb_model)


def get_top_risk_factors(
    transaction_df: pd.DataFrame,
    top_n: int = 5,
) -> list[dict]:
    """
    Return top SHAP contributors for a single transaction.
    """

    shap_values = explainer.shap_values(transaction_df)

    # shap_values shape: (1, n_features)
    values = shap_values[0]

    feature_impacts = []

    for feature, impact in zip(transaction_df.columns, values):
        feature_impacts.append(
            {
                "feature": feature,
                "impact": round(float(impact), 4),
                "abs_impact": abs(float(impact)),
            }
        )

    # Sort by absolute contribution
    feature_impacts.sort(
        key=lambda x: x["abs_impact"],
        reverse=True,
    )

    # Remove helper field
    top_features = []
    for item in feature_impacts[:top_n]:
        top_features.append(
            {
                "feature": item["feature"],
                "impact": item["impact"],
            }
        )

    return top_features