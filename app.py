from flask import Flask, request, jsonify
import joblib
import numpy as np
import joblib
# Initialize Flask app
app = Flask(__name__)


# Define a filename for the exported scaler
scaler_filename = 'scaler.joblib'

# Export the trained scaler object using joblib.dump()
joblib.dump(scaler, scaler_filename)

print(f"StandardScaler object exported successfully to '{scaler_filename}'")
# Load trained model
model = joblib.load("logistic_regression_model.joblib")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "ML Prediction API is running"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()


        features = data.get("features")

        if not features:
            return jsonify({"error": "No features provided"}), 400

        # Convert input to numpy array
        input_data = np.array(features).reshape(1, -1)

        # Prediction
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)

        return jsonify({
            "prediction": int(prediction[0]),
            "probability": probability.tolist()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
