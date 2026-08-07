from flask import Blueprint, jsonify, request
from utils import ChurnPredictionService

# Create Blueprint
api = Blueprint("api", __name__)

# Create prediction service
predictor = ChurnPredictionService()


@api.route("/", methods=["GET"])
def home():
    """
    Health check endpoint.
    """
    return jsonify({
        "message": "Customer Churn Prediction API is Running!",
        "status": "success"
    })


@api.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "No JSON data received."
            }), 400

        prediction, probability = predictor.predict(data)

        return jsonify({

            "prediction": int(prediction),

            "probability": round(float(probability), 4),

            "result": (
                "Customer Will Churn"
                if prediction == 1
                else "Customer Will Stay"
            )

        })

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500