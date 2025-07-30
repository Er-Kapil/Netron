# Arduino Bluetooth Backend API

A Flask backend that connects to Arduino via Bluetooth to receive sensor data (temperature, voltage, vibration) and provides REST API endpoints and WebSocket real-time streaming for frontend applications.

## Features

- 🔗 **Bluetooth Connection**: Connects to Arduino via serial/Bluetooth
- 📊 **Real-time Data**: Receives sensor data continuously
- 🌐 **REST API**: Provides HTTP endpoints for data access
- ⚡ **WebSocket Support**: Real-time data streaming
- 📈 **Data History**: Stores recent readings in memory
- 🔄 **CORS Enabled**: Ready for frontend integration

## API Endpoints

### Connection Management
- `POST /api/connect` - Connect to Arduino
- `POST /api/disconnect` - Disconnect from Arduino
- `GET /api/status` - Get connection status

### Data Access
- `GET /api/data/latest` - Get latest sensor reading
- `GET /api/data/history` - Get historical data
- `GET /api/data/stream` - WebSocket stream info

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure COM port:**
   - Update `config.py` with your Arduino's COM port
   - Default is `COM3`

3. **Run the server:**
   ```bash
   python app.py
   ```

## Arduino Data Format

Your Arduino should send JSON data via Bluetooth:

```json
{
  "temperature": 25.6,
  "voltage": 4.2,
  "vibration": 0
}
```

## Usage Examples

### Connect to Arduino
```bash
curl -X POST http://localhost:5000/api/connect \\
  -H "Content-Type: application/json" \\
  -d '{"port": "COM3", "baudrate": 9600}'
```

### Get Latest Data
```bash
curl http://localhost:5000/api/data/latest
```

### Get Data History
```bash
curl http://localhost:5000/api/data/history?limit=20
```

## WebSocket Real-time Data

Connect to `ws://localhost:5000/socket.io/` and listen for `sensor_data` events:

```javascript
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

socket.on('sensor_data', (data) => {
  console.log('New sensor data:', data);
  // Update your frontend UI
});
```

## Frontend Integration

### React Example
```javascript
import { useEffect, useState } from 'react';
import io from 'socket.io-client';

function SensorDashboard() {
  const [sensorData, setSensorData] = useState(null);
  
  useEffect(() => {
    const socket = io('http://localhost:5000');
    
    socket.on('sensor_data', (data) => {
      setSensorData(data);
    });
    
    return () => socket.disconnect();
  }, []);
  
  return (
    <div>
      <h2>Sensor Data</h2>
      {sensorData && (
        <div>
          <p>Temperature: {sensorData.temperature}°C</p>
          <p>Voltage: {sensorData.voltage}V</p>
          <p>Vibration: {sensorData.vibration ? 'Detected' : 'None'}</p>
        </div>
      )}
    </div>
  );
}
```

## Testing

Run the test client to verify all endpoints:

```bash
python test_client.py
```

## Configuration

Edit `config.py` to customize:
- COM port and baudrate
- Data history limits
- CORS settings
- Server host/port

## Troubleshooting

### Common Issues

1. **Connection Failed**
   - Check COM port in Device Manager
   - Ensure Arduino is paired via Bluetooth
   - Verify baudrate matches Arduino code

2. **No Data Received**
   - Check Arduino serial output
   - Verify JSON format from Arduino
   - Check serial connection stability

3. **CORS Issues**
   - Update CORS origins in `config.py`
   - Ensure frontend URL is allowed

## Production Deployment

1. **Update configuration:**
   ```python
   # config.py
   class ProductionConfig(Config):
       DEBUG = False
       SECRET_KEY = 'your-secure-secret-key'
       CORS_ORIGINS = ["https://your-frontend-domain.com"]
   ```

2. **Use production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -k eventlet -w 1 app:app
   ```

## License

MIT License - Feel free to use in your projects!
