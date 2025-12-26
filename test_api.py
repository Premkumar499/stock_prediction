#!/usr/bin/env python3
"""
Test script for Stock Prediction API
Shows how to send input and get predictions
"""

import requests
import json

# API URL - Change this to your deployed URL
API_URL = "https://stock-prediction-2-tztm.onrender.com"
# For local testing, use: API_URL = "http://localhost:5000"

def test_home():
    """Test the home endpoint to see API documentation"""
    print("=" * 60)
    print("Testing Home Endpoint (GET /)")
    print("=" * 60)
    
    response = requests.get(f"{API_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    print()

def predict_stock_movement(open_price, high_price, low_price, volume):
    """
    Send stock data to API and get prediction
    
    Parameters:
    - open_price: Opening price of the stock
    - high_price: Highest price during the day
    - low_price: Lowest price during the day
    - volume: Trading volume
    
    Returns:
    - 0: Price will decrease (Close < Open)
    - 1: Price will increase (Close > Open)
    """
    print("=" * 60)
    print(f"Making Prediction")
    print("=" * 60)
    print(f"Input Features:")
    print(f"  Open Price:  ${open_price}")
    print(f"  High Price:  ${high_price}")
    print(f"  Low Price:   ${low_price}")
    print(f"  Volume:      {volume:,}")
    print()
    
    # Prepare the request data
    data = {
        "features": [open_price, high_price, low_price, volume]
    }
    
    # Send POST request to /predict endpoint
    response = requests.post(
        f"{API_URL}/predict",
        headers={"Content-Type": "application/json"},
        json=data
    )
    
    # Parse the response
    result = response.json()
    prediction = result.get("prediction")
    
    print(f"API Response: {result}")
    print(f"Prediction: {prediction}")
    
    if prediction == 1:
        print("📈 PREDICTION: Price will INCREASE (Close > Open)")
    else:
        print("📉 PREDICTION: Price will DECREASE (Close < Open)")
    
    print()
    return prediction

if __name__ == "__main__":
    print("\n🚀 Stock Prediction API Test\n")
    
    # Test 1: Check API is running
    test_home()
    
    # Test 2: Example 1 - Bullish scenario (high > open, likely increase)
    print("Test Case 1: Bullish Scenario")
    predict_stock_movement(
        open_price=450.5,
        high_price=455.0,
        low_price=448.0,
        volume=5000000
    )
    
    # Test 3: Example 2 - Bearish scenario (high close to open, likely decrease)
    print("Test Case 2: Bearish Scenario")
    predict_stock_movement(
        open_price=455.0,
        high_price=456.0,
        low_price=445.0,
        volume=6000000
    )
    
    # Test 4: Example 3 - High volume bullish
    print("Test Case 3: High Volume Bullish")
    predict_stock_movement(
        open_price=500.0,
        high_price=510.0,
        low_price=498.0,
        volume=10000000
    )
    
    print("=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)
