from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

model = joblib.load("logistic_regression_model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route("/")
def home():
    return {"status": "Stock Prediction API running"}

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
