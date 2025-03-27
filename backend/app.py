from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Testing Tool Backend API"})

@app.route('/api/test', methods=['POST'])
def run_test():
    try:
        data = request.get_json()
        # Add your test logic here
        return jsonify({
            "status": "success",
            "message": "Test completed successfully",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)