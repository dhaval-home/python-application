from flask import Flask, jsonify
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    """About endpoint - returns service information"""
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({
        "service": "about-service",
        "description": "This is the About Service for the microservices lab",
        "port": 8081,
        "hostname": hostname,
        "version": "1.0",
        "team": "DevOps Lab Team",
        "timestamp": current_time,
        "features": [
            "Service information",
            "Health monitoring",
            "Container-based deployment"
        ]
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "service": "about-service",
        "status": "healthy",
        "port": 8081,
        "uptime": "running"
    }), 200

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        "service": "about-service",
        "endpoints": ["/about", "/health"],
        "port": 8081
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=port, debug=False)
