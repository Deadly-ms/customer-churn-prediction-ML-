"""
predict.py

Purpose:
--------
Load the saved model and predict customer churn.
"""

import joblib
import pandas as pd

from config import (
    MODEL_PATH,
    SCALER_PATH,
    FEATURE_COLUMNS_PATH
)


class ChurnPredictor:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        self.scaler = joblib.load(SCALER_PATH)

        self.feature_columns = joblib.load(FEATURE_COLUMNS_PATH)

    def preprocess(self, customer):

        df = pd.DataFrame([customer])

        # One-Hot Encoding
        df = pd.get_dummies(df)

        # Add missing columns
        for column in self.feature_columns:

            if column not in df.columns:
                df[column] = 0

        # Keep same order
        df = df[self.feature_columns]

        # Scale
        df = self.scaler.transform(df)

        return df

    def predict(self, customer):

        processed = self.preprocess(customer)

        prediction = self.model.predict(processed)[0]

        probability = self.model.predict_proba(processed)[0][1]

        return prediction, probability


if __name__ == "__main__":

    predictor = ChurnPredictor()

    customer = {

        "SeniorCitizen": 0,
        "tenure": 12,
        "MonthlyCharges": 65,
        "TotalCharges": 780,

        "gender": "Male",
        "Partner": "No",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check"

    }

    prediction, probability = predictor.predict(customer)

    print("=" * 50)

    print("Prediction")

    print("=" * 50)

    if prediction == 1:
        print("Customer Will Churn")
    else:
        print("Customer Will Stay")

    print(f"Probability : {probability:.2%}")