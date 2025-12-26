# 🚀 Deployment Guide for Render

## ✅ Pre-deployment Checklist

All issues have been fixed:
- ✅ Models regenerated with matching scikit-learn version (1.5.2)
- ✅ Scaler.joblib fixed (was corrupted)
- ✅ Requirements.txt updated with all dependencies
- ✅ Flask app tested locally - working perfectly
- ✅ Git repository updated and pushed to GitHub

## 📋 Deployment Steps

### Step 1: Go to Render Dashboard
1. Visit: https://dashboard.render.com/
2. Log in with your account (or sign up for free)

### Step 2: Create New Web Service
1. Click the **"New +"** button in the top right
2. Select **"Web Service"**

### Step 3: Connect GitHub Repository
1. Click **"Connect GitHub account"** (if not already connected)
2. Search for your repository: **stock_prediction**
3. Click **"Connect"** next to the repository

### Step 4: Configure Service
Render should auto-detect the `render.yaml` configuration. Verify these settings:

- **Name**: `stock-prediction-1` (or choose your own)
- **Region**: Oregon (or closest to you)
- **Branch**: `main`
- **Runtime**: Python
- **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
- **Plan**: Free

### Step 5: Deploy
1. Click **"Create Web Service"** or **"Apply"**
2. Wait for the deployment (usually 2-5 minutes)
3. Watch the logs for any errors

### Step 6: Test Your Deployment
Once deployed, you'll get a URL like: `https://stock-prediction-1.onrender.com`

Test it with:
```bash
# Check status
curl https://your-app-name.onrender.com/

# Make a prediction
curl -X POST https://your-app-name.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [450.5, 455.0, 448.0, 5000000]}'
```

## 🔍 Troubleshooting

### If deployment fails:

1. **Check the logs** in Render dashboard
2. **Verify files are in repository**:
   - app.py
   - requirements.txt
   - render.yaml
   - runtime.txt
   - logistic_regression_model.joblib
   - scaler.joblib

3. **Common issues**:
   - Missing model files: Make sure `.joblib` files are committed
   - Python version: Render uses Python 3.11.10 (specified in runtime.txt)
   - Port binding: App uses `os.environ.get("PORT", 5000)`

## ⚠️ Important Notes

1. **Free Tier Limitations**:
   - Service spins down after 15 minutes of inactivity
   - First request after spin-down will be slow (~30 seconds)
   - 750 hours/month of runtime

2. **Model Files**:
   - Total size: ~1.5KB (very small, good for deployment)
   - Both .joblib files are required

3. **Environment**:
   - Python 3.11.10
   - All dependencies from requirements.txt are automatically installed

## 🎉 Success!

Your API should be live and accessible. Share the URL with anyone who needs to make predictions!

## 📊 Example Usage

```python
import requests

url = "https://your-app-name.onrender.com/predict"
data = {
    "features": [450.5, 455.0, 448.0, 5000000]  # [Open, High, Low, Volume]
}

response = requests.post(url, json=data)
print(response.json())  # {'prediction': 1}
```
