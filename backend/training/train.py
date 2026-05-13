import warnings
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import average_precision_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

warnings.filterwarnings("ignore")


# =========================================================
# Paths
# =========================================================
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "creditcard.csv"

MODEL_DIR = PROJECT_ROOT / "models"
XGB_DIR = MODEL_DIR / "xgboost_model"
ANOMALY_DIR = MODEL_DIR / "anomaly_detector"

XGB_DIR.mkdir(parents=True, exist_ok=True)
ANOMALY_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# Load Data
# =========================================================
print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

X = df.drop(columns=["Class"])
y = df["Class"]

print(f"Dataset shape: {df.shape}")
print(f"Fraud cases: {y.sum()}")
print(f"Fraud ratio: {y.mean():.6f}")


# =========================================================
# Train-Test Split
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print(f"Train shape: {X_train.shape}")
print(f"Test shape: {X_test.shape}")


# =========================================================
# XGBoost Classifier
# =========================================================
print("\nTraining XGBoost model...")

scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

xgb_model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="aucpr",
    scale_pos_weight=scale_pos_weight,
    random_state=42,
    n_jobs=-1,
)

xgb_model.fit(X_train, y_train)

# Predictions
y_proba = xgb_model.predict_proba(X_test)[:, 1]
y_pred = (y_proba >= 0.5).astype(int)

# Metrics
roc_auc = roc_auc_score(y_test, y_proba)
pr_auc = average_precision_score(y_test, y_proba)

print(f"ROC-AUC: {roc_auc:.6f}")
print(f"PR-AUC: {pr_auc:.6f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, digits=4))


# =========================================================
# Isolation Forest
# =========================================================
print("\nTraining Isolation Forest...")

iso_model = IsolationForest(
    n_estimators=200,
    contamination=0.0017,  # ~ fraud ratio
    random_state=42,
    n_jobs=-1,
)

# Train on normal transactions only
X_train_normal = X_train[y_train == 0]
iso_model.fit(X_train_normal)

print("Isolation Forest training completed.")


# =========================================================
# Save Artifacts
# =========================================================
print("\nSaving artifacts...")

joblib.dump(xgb_model, XGB_DIR / "xgboost_model.joblib")
joblib.dump(iso_model, ANOMALY_DIR / "isolation_forest.joblib")
joblib.dump(list(X.columns), MODEL_DIR / "feature_columns.joblib")

print("Saved:")
print(f"- {XGB_DIR / 'xgboost_model.joblib'}")
print(f"- {ANOMALY_DIR / 'isolation_forest.joblib'}")
print(f"- {MODEL_DIR / 'feature_columns.joblib'}")

print("\nTraining completed successfully.")