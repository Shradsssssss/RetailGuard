from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all origins

# Load trained model
model = joblib.load("model.pkl")  # Make sure this file exists!

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400

        # Extract input values from JSON
        input_vector = np.array([[
            data.get("session_time", 0),
            data.get("clicks", 0),
            data.get("cart_adds", 0),
            data.get("reviews", 0),
        ]])

        # Make prediction
        prediction = model.predict_proba(input_vector)[0][1]  # Probability of being a bot
        is_bot = bool(prediction > 0.7)

        # Return result
        return jsonify({
            "risk_score": round(float(prediction), 3),
            "is_bot": is_bot
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
