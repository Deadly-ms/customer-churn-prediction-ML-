"""
feature_engineering.py

Purpose:
--------
Prepare the cleaned dataset for machine learning.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from config import CLEAN_DATASET_PATH


class FeatureEngineer:

    def __init__(self):
        self.scaler = StandardScaler()

    def load_dataset(self):
        """
        Load cleaned dataset.
        """
        df = pd.read_csv(CLEAN_DATASET_PATH)

        print("=" * 50)
        print("Clean Dataset Loaded Successfully")
        print("=" * 50)

        return df

    def split_features_target(self, df):
        """
        Split into X and y.
        """

        X = df.drop("Churn", axis=1)
        y = df["Churn"]

        return X, y

    def encode_target(self, y):
        """
        Convert target labels to numeric.
        """

        y = y.map({
            "No": 0,
            "Yes": 1
        })

        return y

    def encode_features(self, X):
        """
        One-Hot Encode categorical columns.
        """

        X = pd.get_dummies(
            X,
            drop_first=True
        )

        return X

    def train_test(self, X, y):
        """
        Split into train and test.
        """

        return train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

    def scale_data(self, X_train, X_test):
        """
        Standardize features.
        """

        X_train_scaled = self.scaler.fit_transform(X_train)

        X_test_scaled = self.scaler.transform(X_test)

        return X_train_scaled, X_test_scaled


if __name__ == "__main__":

    engineer = FeatureEngineer()

    df = engineer.load_dataset()

    X, y = engineer.split_features_target(df)

    y = engineer.encode_target(y)

    X = engineer.encode_features(X)

    feature_columns = X.columns.tolist()

    X_train, X_test, y_train, y_test = engineer.train_test(X, y)

    X_train, X_test = engineer.scale_data(X_train, X_test)

    print("\nTraining Shape :", X_train.shape)
    print("Testing Shape  :", X_test.shape)
    print("Number of Features :", len(feature_columns))

    print("\nFeature Engineering Completed Successfully.")