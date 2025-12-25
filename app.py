from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# Paths
MODEL_PATH = "logistic_regression_model.joblib"
SCALER_PATH = "scaler.joblib"

# Load model & scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

@app.route("/")
def home():
    return jsonify({"message": "Stock Prediction API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if "features" not in data:
            return jsonify({"error": "features key missing"}), 400

        X = np.array(data["features"]).reshape(1, -1)
        X_scaled = scaler.transform(X)

        prediction = int(model.predict(X_scaled)[0])
        probability = model.predict_proba(X_scaled)[0].tolist()

        return jsonify({
            "prediction": prediction,
            "probability": probability
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
