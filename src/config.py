import os

# Project Root Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset Path
DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# Clean Dataset Path
CLEAN_DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "cleaned_telco_churn.csv"
)

# Model Folder
MODEL_DIR = os.path.join(BASE_DIR, "model")

# Saved Model
MODEL_PATH = os.path.join(
    MODEL_DIR,
    "churn_model.pkl"
)

# Scaler
SCALER_PATH = os.path.join(
    MODEL_DIR,
    "scaler.pkl"
)

# Feature Columns
FEATURE_COLUMNS_PATH = os.path.join(
    MODEL_DIR,
    "feature_columns.pkl"
)