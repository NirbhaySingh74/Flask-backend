from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the URL from the environment variable
AMPLIFY_URL = os.getenv('AMPLIFY_URL')

# Endpoint to fetch all items
@app.route('/', methods=['GET'])
def get_items():
    response = requests.get(AMPLIFY_URL)
    return jsonify(response.json())

# Endpoint to fetch a specific item by id
@app.route('/items/<int:id>', methods=['GET'])
def get_item_by_id(id):
    response = requests.get(AMPLIFY_URL)
    items = response.json()
    item = next((item for item in items if item['id'] == id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)