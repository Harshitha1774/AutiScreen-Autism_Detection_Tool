from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# Select database and collection
db = client["autism_app"]
responses = db["responses"]

# Initialize Flask
app = Flask(__name__)
CORS(app)  # allows React frontend to talk to Flask

@app.route("/")
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route("/add", methods=["POST"])
def add_response():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Insert into MongoDB
    responses.insert_one(data)
    return jsonify({"message": "Data inserted successfully!"})

@app.route("/get", methods=["GET"])
def get_responses():
    all_responses = list(responses.find({}, {"_id": 0}))  # don’t send MongoDB’s _id
    return jsonify(all_responses)

if __name__ == "__main__":
    app.run(debug=True)
