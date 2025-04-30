from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.before_request
def before_request():
    logger.debug(f"Request received: {request.method} {request.url}")
    logger.debug(f"Headers: {request.headers}")
    logger.debug(f"Origin: {request.headers.get('Origin')}")

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.route('/api/hello', methods=['GET', 'OPTIONS'])
def hello():
    try:
        if request.method == 'OPTIONS':
            return '', 200
        logger.debug("Processing /api/hello request")
        return jsonify({"message": "Hello from Flask!"})
    except Exception as e:
        logger.error(f"Error in /api/hello: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
