import os
from flask import Flask, send_from_directory
from flask_cors import CORS

from routes import api

FRONTEND_DIST = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend", "dist")
)

app = Flask(
    __name__,
    static_folder=os.path.join(FRONTEND_DIST, "assets") if os.path.exists(os.path.join(FRONTEND_DIST, "assets")) else None,
    static_url_path="/assets"
)

# Allow requests from React frontend
CORS(app)

# Register API routes
app.register_blueprint(api)


@app.route("/", methods=["GET"])
def index():
    index_file = os.path.join(FRONTEND_DIST, "index.html")
    if os.path.exists(index_file):
        return send_from_directory(FRONTEND_DIST, "index.html")
    return {
        "message": "Customer Churn Prediction API is Running!",
        "status": "success"
    }


@app.route("/<path:path>", methods=["GET"])
def static_proxy(path):
    file_path = os.path.join(FRONTEND_DIST, path)
    if os.path.exists(file_path):
        return send_from_directory(FRONTEND_DIST, path)
    index_file = os.path.join(FRONTEND_DIST, "index.html")
    if os.path.exists(index_file):
        return send_from_directory(FRONTEND_DIST, "index.html")
    return {"error": "Not Found"}, 404

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5050)),
        debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    )