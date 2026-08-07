from flask import Flask
from flask_cors import CORS

from routes import api

app = Flask(__name__)

# Allow requests from React frontend
CORS(app)

# Register API routes
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5050,
        debug=True
    )