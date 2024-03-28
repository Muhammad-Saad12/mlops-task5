from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.json['name']
    email = request.json['email']
    if name and email:
        mongo.db.users.insert_one({'name': name, 'email': email})
        return jsonify({'msg': 'User added successfully'}), 201
    else:
        return jsonify({'msg': 'Missing data'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
