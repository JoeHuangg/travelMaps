from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
import os
from bson import ObjectId

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Change this to something more secure

# Initialize extensions
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# MongoDB setup (Assuming it's running locally. Replace URI if using a hosted MongoDB like Atlas)
client = MongoClient('mongodb://localhost:27017/')
db = client.travel_tracker
users_collection = db.users

# Registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Check if user already exists
    if users_collection.find_one({"username": username}):
        return jsonify({"msg": "User already exists"}), 400

    # Hash password and save the user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = {
        "username": username,
        "password": hashed_password,
        "visited_states": []
    }
    users_collection.insert_one(new_user)
    return jsonify({"msg": "User registered successfully"}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = users_collection.find_one({"username": username})
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"msg": "Invalid credentials"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=str(user['_id']))
    return jsonify(access_token=access_token), 200

# Save visited states
@app.route('/save', methods=['POST'])
@jwt_required()
def save_progress():
    data = request.get_json()
    visited_states = data.get('visitedStates', [])  # Get the visited states from the request body

    # Get the logged-in user's ID from the JWT token
    user_id = get_jwt_identity()

    # Update the user's visited states in the database
    try:
        users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": {"visited_states": visited_states}})
    except Exception as e:
        return jsonify({"msg": "Error saving progress"}), 500

    return jsonify({"msg": "Progress saved"}), 200

# Get visited states
@app.route('/progress', methods=['GET'])
@jwt_required()
def get_progress():
    user_id = get_jwt_identity()  # Get the user_id from JWT

    try:
        # Convert the user_id string to ObjectId
        user = users_collection.find_one({"_id": ObjectId(user_id)})
    except Exception as e:
        return jsonify({"msg": "Invalid user ID format"}), 400

    if user:
        return jsonify(visited_states=user['visited_states']), 200
    else:
        return jsonify({"msg": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
