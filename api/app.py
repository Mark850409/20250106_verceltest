from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "LangFlow is running on Vercel!"})

@app.route('/langflow', methods=['POST'])
def langflow():
    # Simulate LangFlow functionality (replace with actual logic)
    data = request.json
    response = {"received": data, "response": "Processed by LangFlow"}
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
