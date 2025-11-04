from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    """Hello endpoint - returns greeting message"""
    hostname = socket.gethostname()
    return jsonify({
        "service": "hello-service",
        "message": "Hello from the Hello Service!",
        "port": 8080,
        "hostname": hostname,
        "version": "1.0"
    }), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "service": "hello-service",
        "status": "healthy",
        "port": 8080
    }), 200

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        "service": "hello-service",
        "endpoints": ["/hello", "/health"],
        "port": 8080
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
