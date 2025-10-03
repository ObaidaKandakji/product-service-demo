from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Enable CORS: allow any origin, restrict methods to GET
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])

@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

if __name__ == "__main__":
    # Read host/port from environment variables, fallback to defaults
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 3030))
    
    app.run(host=host, port=port)

