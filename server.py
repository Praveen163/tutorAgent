from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import asyncio
from src.app import tutor_managerr
import os
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__)
CORS(app)

# Helper to run async agent in sync Flask context
def run_async(coro):
    return asyncio.get_event_loop().run_until_complete(coro)

@app.route('/chat', methods=['POST'])
async def chat():
    data = request.json
    message = data.get('message')
    history = data.get('history', [])
    # Format messages as needed for the agent (if required)
    # Here, we just pass the message; adapt if agent supports histor
    result = await tutor_managerr(message, history)
    return jsonify({'response': result})

@app.route('/')
def serve_index():
    return send_from_directory('./static', 'index.html')

@app.route('/check')
def serve_check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 as per Render docs
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True) 