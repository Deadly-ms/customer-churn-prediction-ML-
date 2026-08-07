"""
save_model.py

Purpose:
--------
Save the trained model, scaler, and feature columns.
"""

import os
import joblib

from feature_engineering import FeatureEngineer
from train_model import ModelTrainer
from config import (
    MODEL_DIR,
    MODEL_PATH,
    SCALER_PATH,
    FEATURE_COLUMNS_PATH
)


class ModelSaver:

    def __init__(self):
        os.makedirs(MODEL_DIR, exist_ok=True)

    def save(self, model, scaler, feature_columns):

        joblib.dump(model, MODEL_PATH)

        joblib.dump(scaler, SCALER_PATH)

        joblib.dump(feature_columns, FEATURE_COLUMNS_PATH)

        print("\nModel saved successfully!")
        print(f"Model    : {MODEL_PATH}")
        print(f"Scaler   : {SCALER_PATH}")
        print(f"Features : {FEATURE_COLUMNS_PATH}")


if __name__ == "__main__":

    # Feature Engineering
    engineer = FeatureEngineer()

    df = engineer.load_dataset()

    X, y = engineer.split_features_target(df)

    y = engineer.encode_target(y)

    X = engineer.encode_features(X)

    feature_columns = X.columns.tolist()

    X_train, X_test, y_train, y_test = engineer.train_test(X, y)

    X_train, X_test = engineer.scale_data(X_train, X_test)

    # Train Models
    trainer = ModelTrainer()

    trained_models = trainer.train_models(X_train, y_train)

    scores = trainer.evaluate_models(
        trained_models,
        X_test,
        y_test
    )

    best_model = trainer.best_model(
        trained_models,
        scores
    )

    # Save Everything
    saver = ModelSaver()

    saver.save(
        best_model,
        engineer.scaler,
        feature_columns
    )

    print("\nAll files saved successfully.")