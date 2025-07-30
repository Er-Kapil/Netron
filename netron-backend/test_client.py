#!/usr/bin/env python3
"""
Test client to verify the Flask backend API endpoints
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_api_endpoints():
    """Test all API endpoints"""
    
    print("🧪 Testing Arduino Bluetooth Backend API")
    print("=" * 50)
    
    # Test 1: Check server status
    print("\\n1. Testing server status...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Server Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Server connection failed: {e}")
        return
    
    # Test 2: Check connection status
    print("\\n2. Testing connection status...")
    try:
        response = requests.get(f"{BASE_URL}/api/status")
        print(f"✅ Connection Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Status check failed: {e}")
    
    # Test 3: Try to connect to Arduino
    print("\\n3. Testing Arduino connection...")
    try:
        connect_data = {
            "port": "COM3",  # Change this to your Arduino's COM port
            "baudrate": 9600
        }
        response = requests.post(f"{BASE_URL}/api/connect", json=connect_data)
        print(f"📡 Connect attempt: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Connection attempt failed: {e}")
    
    # Test 4: Get latest data
    print("\\n4. Testing latest data endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/data/latest")
        print(f"📊 Latest data: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Latest data request failed: {e}")
    
    # Test 5: Get data history
    print("\\n5. Testing data history endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/data/history?limit=10")
        print(f"📈 Data history: {response.status_code}")
        data = response.json()
        print(f"   Count: {data.get('count', 0)} records")
    except Exception as e:
        print(f"❌ Data history request failed: {e}")
    
    # Test 6: Stream info
    print("\\n6. Testing stream endpoint info...")
    try:
        response = requests.get(f"{BASE_URL}/api/data/stream")
        print(f"🌊 Stream info: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Stream info request failed: {e}")
    
    print("\\n" + "=" * 50)
    print("✅ API testing completed!")

def simulate_arduino_data():
    """Simulate Arduino data for testing (when no Arduino is connected)"""
    import random
    
    sample_data = {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "voltage": round(random.uniform(3.0, 5.0), 2),
        "vibration": random.choice([0, 1])
    }
    
    return json.dumps(sample_data)

if __name__ == "__main__":
    print("🚀 Starting API tests...")
    test_api_endpoints()
    
    print("\\n💡 To test with simulated data:")
    print("   1. Make sure the Flask server is running")
    print("   2. If no Arduino is connected, the API will still work")
    print("   3. Use WebSocket client to test real-time data")
    
    print("\\n📝 Sample Arduino data format:")
    print(f"   {simulate_arduino_data()}")
