import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get MongoDB URI
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Create database & collection
db = client["autism_app"]         # database name
responses = db["responses"]       # collection name
