from pathlib import Path

import joblib


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Model artifact paths
MODEL_DIR = PROJECT_ROOT / "models"
XGB_MODEL_PATH = MODEL_DIR / "xgboost_model" / "xgboost_model.joblib"
ISO_MODEL_PATH = MODEL_DIR / "anomaly_detector" / "isolation_forest.joblib"
FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.joblib"


class ModelLoader:
    """
    Loads and stores all model artifacts in memory.
    """

    def __init__(self) -> None:
        self.xgb_model = None
        self.iso_model = None
        self.feature_columns = None
        self._load_artifacts()

    def _load_artifacts(self) -> None:
        print("Loading model artifacts...")

        self.xgb_model = joblib.load(XGB_MODEL_PATH)
        self.iso_model = joblib.load(ISO_MODEL_PATH)
        self.feature_columns = joblib.load(FEATURE_COLUMNS_PATH)

        print("Artifacts loaded successfully.")


# Singleton instance
model_loader = ModelLoader()