# Configuration settings for the Arduino Bluetooth Backend

class Config:
    # Flask settings
    SECRET_KEY = 'your-secret-key-change-this-in-production'
    DEBUG = True
    
    # Bluetooth settings
    DEFAULT_COM_PORT = 'COM3'  # Change this to your Arduino's COM port
    DEFAULT_BAUDRATE = 9600
    
    # Data settings
    MAX_DATA_HISTORY = 100  # Maximum number of readings to store in memory
    DATA_READ_INTERVAL = 0.1  # Seconds between data reads
    
    # CORS settings
    CORS_ORIGINS = "*"  # In production, specify your frontend domain
    
    # Server settings
    HOST = '0.0.0.0'
    PORT = 5000

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'your-production-secret-key'
    CORS_ORIGINS = ["http://localhost:3000", "http://your-frontend-domain.com"]

# Default configuration
config = DevelopmentConfig
