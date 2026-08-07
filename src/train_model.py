"""
train_model.py

Purpose:
--------
Train multiple machine learning models and select the best one.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from feature_engineering import FeatureEngineer


class ModelTrainer:

    def __init__(self):
        self.models = {
            "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
            "Decision Tree": DecisionTreeClassifier(random_state=42),
            "Random Forest": RandomForestClassifier(random_state=42)
        }

    def train_models(self, X_train, y_train):

        trained_models = {}

        print("=" * 60)
        print("Training Models")
        print("=" * 60)

        for name, model in self.models.items():

            model.fit(X_train, y_train)

            trained_models[name] = model

            print(f"{name} trained successfully.")

        return trained_models

    def evaluate_models(self, trained_models, X_test, y_test):

        print("\n")
        print("=" * 60)
        print("Model Accuracy")
        print("=" * 60)

        scores = {}

        for name, model in trained_models.items():

            predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)

            scores[name] = accuracy

            print(f"{name:<25}: {accuracy:.4f}")

        return scores

    def best_model(self, trained_models, scores):

        best_name = max(scores, key=scores.get)

        print("\nBest Model :", best_name)

        return trained_models[best_name]


if __name__ == "__main__":

    engineer = FeatureEngineer()

    df = engineer.load_dataset()

    X, y = engineer.split_features_target(df)

    y = engineer.encode_target(y)

    X = engineer.encode_features(X)

    feature_columns = X.columns.tolist()

    X_train, X_test, y_train, y_test = engineer.train_test(X, y)

    X_train, X_test = engineer.scale_data(X_train, X_test)

    trainer = ModelTrainer()

    trained_models = trainer.train_models(
        X_train,
        y_train
    )

    scores = trainer.evaluate_models(
        trained_models,
        X_test,
        y_test
    )

    best_model = trainer.best_model(
        trained_models,
        scores
    )

    print("\nTraining Completed Successfully.")