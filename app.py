from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

model = joblib.load("logistic_regression_model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route("/")
def home():
    return jsonify({
        "status": "Stock Prediction API running",
        "endpoints": {
            "POST /predict": "Make a stock price prediction"
        },
        "usage": {
            "method": "POST",
            "url": "/predict",
            "content_type": "application/json",
            "input": {
                "features": "[Open, High, Low, Volume]"
            },
            "example_request": {
                "features": [450.5, 455.0, 448.0, 5000000]
            },
            "example_response": {
                "prediction": 1,
                "meaning": "0 = Price will decrease, 1 = Price will increase"
            }
        },
        "curl_example": "curl -X POST https://stock-prediction-2-tztm.onrender.com/predict -H 'Content-Type: application/json' -d '{\"features\": [450.5, 455.0, 448.0, 5000000]}'"
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X = np.array(data["features"]).reshape(1, -1)
    X = scaler.transform(X)
    pred = int(model.predict(X)[0])
    return {"prediction": pred}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
