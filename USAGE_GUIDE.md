# 📊 How to Use the Stock Prediction API

## 🎯 What This API Does

Predicts whether a stock's closing price will be **higher** or **lower** than its opening price based on:
- **Open Price**: Starting price
- **High Price**: Highest price during trading
- **Low Price**: Lowest price during trading  
- **Volume**: Number of shares traded

## 🌐 Your Live API

**URL**: https://stock-prediction-2-tztm.onrender.com

## 📝 How to Give Input and Get Output

### Method 1: Using cURL (Command Line)

```bash
curl -X POST https://stock-prediction-2-tztm.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [450.5, 455.0, 448.0, 5000000]}'
```

**Output:**
```json
{"prediction": 1}
```
- `0` = Price will **DECREASE** 📉
- `1` = Price will **INCREASE** 📈

### Method 2: Using Python

```python
import requests

# Your stock data
stock_data = {
    "features": [
        450.5,     # Open price
        455.0,     # High price
        448.0,     # Low price
        5000000    # Volume
    ]
}

# Make prediction
response = requests.post(
    "https://stock-prediction-2-tztm.onrender.com/predict",
    json=stock_data
)

result = response.json()
print(f"Prediction: {result['prediction']}")

if result['prediction'] == 1:
    print("📈 Stock price will INCREASE")
else:
    print("📉 Stock price will DECREASE")
```

### Method 3: Using JavaScript

```javascript
fetch('https://stock-prediction-2-tztm.onrender.com/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    features: [450.5, 455.0, 448.0, 5000000]
  })
})
.then(response => response.json())
.then(data => {
  console.log('Prediction:', data.prediction);
  if (data.prediction === 1) {
    console.log('📈 Stock price will INCREASE');
  } else {
    console.log('📉 Stock price will DECREASE');
  }
});
```

### Method 4: Using Postman

1. Set method to **POST**
2. URL: `https://stock-prediction-2-tztm.onrender.com/predict`
3. Headers: `Content-Type: application/json`
4. Body (raw JSON):
```json
{
  "features": [450.5, 455.0, 448.0, 5000000]
}
```
5. Click **Send**

## 📋 Input Format

The `features` array must have exactly **4 numbers** in this order:

```json
{
  "features": [Open, High, Low, Volume]
}
```

### Example Inputs:

**Bullish Scenario (likely to increase):**
```json
{"features": [450.5, 455.0, 448.0, 5000000]}
```

**Bearish Scenario (likely to decrease):**
```json
{"features": [455.0, 456.0, 445.0, 6000000]}
```

**High Volume Trade:**
```json
{"features": [500.0, 510.0, 498.0, 10000000]}
```

## 🧪 Test the API

Run the included test script:
```bash
python test_api.py
```

This will show you:
- How to format inputs
- How to parse outputs
- Multiple example predictions

## 📖 API Documentation

Visit the home page for full documentation:
```bash
curl https://stock-prediction-2-tztm.onrender.com/
```

## ⚡ Quick Test

Open your browser and visit:
- **API Status**: https://stock-prediction-2-tztm.onrender.com/

Then use any method above to make predictions!

## 💡 Tips

1. **Volume** should be in actual number of shares (e.g., 5000000, not 5M)
2. **Prices** can have decimals (e.g., 450.5)
3. API responds in **under 1 second** when active
4. First request after inactivity may take ~30 seconds (free tier)

## 🔍 Understanding Predictions

- **Prediction: 1** → Closing price > Opening price (Buy signal)
- **Prediction: 0** → Closing price < Opening price (Sell signal)

**Model Accuracy**: ~83.66%
