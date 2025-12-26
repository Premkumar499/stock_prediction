# Stock Prediction API

A Flask-based REST API that predicts stock price movements using a Logistic Regression model trained on Netflix stock data.

## Features
- Predicts whether stock price will increase or decrease
- Uses Open, High, Low, and Volume features
- RESTful API endpoints
- Ready for deployment on Render

## Local Development

### Setup
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run locally
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Test the API
```bash
# Check status
curl http://localhost:5000/

# Make a prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [450.5, 455.0, 448.0, 5000000]}'
```

## Deployment on Render

### Prerequisites
1. A GitHub account
2. A Render account (free tier available)

### Steps

1. **Initialize Git repository** (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. **Push to GitHub**:
```bash
# Create a new repository on GitHub, then:
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```

3. **Deploy on Render**:
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` configuration
   - Click "Apply" to deploy

4. **Your API will be live** at: `https://your-app-name.onrender.com`

## API Endpoints

### GET /
Health check endpoint
```json
{
  "status": "Stock Prediction API running"
}
```

### POST /predict
Make a stock prediction

**Request body:**
```json
{
  "features": [open_price, high_price, low_price, volume]
}
```

**Example:**
```json
{
  "features": [450.5, 455.0, 448.0, 5000000]
}
```

**Response:**
```json
{
  "prediction": 1
}
```
- `0`: Price will decrease (Close < Open)
- `1`: Price will increase (Close > Open)

## Model Information
- **Algorithm**: Logistic Regression
- **Features**: Open, High, Low, Volume
- **Target**: Binary classification (price increase/decrease)
- **Accuracy**: ~83.66%

## Files
- `app.py`: Flask application
- `logistic_regression_model.joblib`: Trained model
- `scaler.joblib`: Feature scaler
- `requirements.txt`: Python dependencies
- `render.yaml`: Render deployment configuration
- `runtime.txt`: Python version specification
