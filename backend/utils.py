import os
import sys
import joblib
import pandas as pd

# ----------------------------------------------------
# Add project root to Python path
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from src.config import (
    MODEL_PATH,
    SCALER_PATH,
    FEATURE_COLUMNS_PATH
)


class ChurnPredictionService:

    def __init__(self):

        print("Loading trained model...")

        self.model = joblib.load(MODEL_PATH)

        self.scaler = joblib.load(SCALER_PATH)

        self.feature_columns = joblib.load(FEATURE_COLUMNS_PATH)

        print("Model loaded successfully.")

    def preprocess(self, customer):

        df = pd.DataFrame([customer])

        # One-Hot Encoding
        df = pd.get_dummies(df)

        # Add missing columns
        for column in self.feature_columns:

            if column not in df.columns:
                df[column] = 0

        # Remove extra columns
        df = df.reindex(
            columns=self.feature_columns,
            fill_value=0
        )

        # Scale
        df = self.scaler.transform(df)

        return df

    def predict(self, customer):

        processed = self.preprocess(customer)

        prediction = self.model.predict(processed)[0]

        probability = self.model.predict_proba(processed)[0][1]

        return prediction, probability