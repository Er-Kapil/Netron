from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import serial
import json
import threading
import time
from datetime import datetime
import logging
from collections import deque

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
CORS(app)  # Enable CORS for all routes
socketio = SocketIO(app, cors_allowed_origins="*")

class BluetoothManager:
    def __init__(self):
        self.serial_connection = None
        self.is_connected = False
        self.reading_thread = None
        self.latest_data = {
            'temperature': None,
            'voltage': None,
            'vibration': None,
            'timestamp': None
        }
        self.data_history = deque(maxlen=100)  # Store last 100 readings
        
    def connect(self, port='COM3', baudrate=9600):
        """Connect to Arduino via Bluetooth"""
        try:
            if self.is_connected:
                logger.info("Already connected")
                return True
                
            self.serial_connection = serial.Serial(port, baudrate, timeout=1)
            self.is_connected = True
            logger.info(f"Connected to {port}")
            
            # Start reading thread
            self.reading_thread = threading.Thread(target=self._read_data, daemon=True)
            self.reading_thread.start()
            
            return True
        except Exception as e:
            logger.error(f"Failed to connect: {str(e)}")
            return False
    
    def disconnect(self):
        """Disconnect from Arduino"""
        self.is_connected = False
        if self.serial_connection:
            self.serial_connection.close()
            logger.info("Disconnected from Arduino")
    
    def _read_data(self):
        """Continuously read data from Arduino"""
        while self.is_connected:
            try:
                if self.serial_connection and self.serial_connection.in_waiting > 0:
                    line = self.serial_connection.readline().decode('utf-8').strip()
                    if line:
                        self._process_data(line)
            except Exception as e:
                logger.error(f"Error reading data: {e}")
            time.sleep(0.1)
    
    def _process_data(self, data_string):
        """Process incoming data from Arduino"""
        try:
            # Parse JSON data from Arduino
            data = json.loads(data_string)
            
            # Add timestamp
            data['timestamp'] = datetime.now().isoformat()
            
            # Update latest data
            self.latest_data = data
            
            # Add to history
            self.data_history.append(data.copy())
            
            # Emit to connected clients via WebSocket
            socketio.emit('sensor_data', data)
            
            logger.info(f"Processed data: {data}")
            
        except json.JSONDecodeError:
            logger.warning(f"Invalid JSON received: {data_string}")
        except Exception as e:
            logger.error(f"Error processing data: {e}")
    
    def get_latest_data(self):
        """Get the latest sensor reading"""
        return self.latest_data
    
    def get_data_history(self, limit=50):
        """Get historical data"""
        return list(self.data_history)[-limit:]

# Initialize Bluetooth manager
bluetooth_manager = BluetoothManager()

# API Routes
@app.route('/')
def index():
    return jsonify({
        'message': 'Arduino Bluetooth Backend API',
        'version': '1.0',
        'status': 'running'
    })

@app.route('/api/connect', methods=['POST'])
def connect_bluetooth():
    """Connect to Arduino via Bluetooth"""
    data = request.get_json() or {}
    port = data.get('port', 'COM3')
    baudrate = data.get('baudrate', 9600)
    
    success = bluetooth_manager.connect(port, baudrate)
    
    return jsonify({
        'success': success,
        'message': f'Connected to {port}' if success else 'Failed to connect',
        'connected': bluetooth_manager.is_connected
    })

@app.route('/api/disconnect', methods=['POST'])
def disconnect_bluetooth():
    """Disconnect from Arduino"""
    bluetooth_manager.disconnect()
    
    return jsonify({
        'success': True,
        'message': 'Disconnected',
        'connected': bluetooth_manager.is_connected
    })

@app.route('/api/status')
def get_status():
    """Get connection status"""
    return jsonify({
        'connected': bluetooth_manager.is_connected,
        'latest_data': bluetooth_manager.get_latest_data()
    })

@app.route('/api/data/latest')
def get_latest_data():
    """Get the latest sensor reading"""
    data = bluetooth_manager.get_latest_data()
    
    if data['timestamp'] is None:
        return jsonify({
            'success': False,
            'message': 'No data available'
        }), 404
    
    return jsonify({
        'success': True,
        'data': data
    })

@app.route('/api/data/history')
def get_data_history():
    """Get historical sensor data"""
    limit = request.args.get('limit', 50, type=int)
    history = bluetooth_manager.get_data_history(limit)
    
    return jsonify({
        'success': True,
        'data': history,
        'count': len(history)
    })

@app.route('/api/data/stream')
def stream_data():
    """Get real-time data stream endpoint info"""
    return jsonify({
        'message': 'Use WebSocket connection for real-time data',
        'websocket_url': '/socket.io/',
        'event': 'sensor_data'
    })

# WebSocket Events
@socketio.on('connect')
def handle_connect():
    logger.info('Client connected to WebSocket')
    emit('status', {
        'connected': bluetooth_manager.is_connected,
        'message': 'Connected to server'
    })

@socketio.on('disconnect')
def handle_disconnect():
    logger.info('Client disconnected from WebSocket')

@socketio.on('request_latest_data')
def handle_request_latest_data():
    """Send latest data to requesting client"""
    data = bluetooth_manager.get_latest_data()
    emit('sensor_data', data)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    # Auto-connect on startup (optional)
    # bluetooth_manager.connect()
    
    logger.info("Starting Flask-SocketIO server...")
    socketio.run(app, debug=True, host='0.0.0.0', port=5000) 
