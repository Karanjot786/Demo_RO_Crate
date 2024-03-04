from flask import Flask, jsonify, request
from pymongo import MongoClient 
import uuid  
from dotenv import load_dotenv  
import os

app = Flask(__name__)

load_dotenv()

connection_string = os.getenv('URL')

# Connect to your MongoDB
client = MongoClient(connection_string)
db = client['rocrate_db'] 
rocrate_collection = db['rocrates'] 


# Placeholder RO-Crate structure 
class ROCrate:
    def __init__(self, title, description, author):
        self.id = str(uuid.uuid4()) 
        self.title = title
        self.description = description
        self.author = author

# Routes for CRUD
@app.route('/rocrate', methods=['POST'])
def create_rocrate():
    data = request.json
    new_rocrate = ROCrate(data['title'], data['description'], data['author'])
    rocrate_collection.insert_one(new_rocrate.__dict__)
    return jsonify({'id': new_rocrate.id}), 201

@app.route('/rocrate/<rocrate_id>')
def get_rocrate(rocrate_id):
    rocrate = rocrate_collection.find_one({'id': rocrate_id})
    if rocrate:
        return jsonify(rocrate)
    else:
        return jsonify({'error': 'RO-Crate not found'}), 404

@app.route('/rocrate/<rocrate_id>', methods=['PUT'])
def update_rocrate(rocrate_id):
    data = request.json  # Get the updated data from the request

    # 1. Find the existing RO-Crate in the database 
    rocrate = rocrate_collection.find_one({'id': rocrate_id})
    if not rocrate:
        return jsonify({'error': 'RO-Crate not found'}), 404

    # 2. Update the fields
    update_query = {'$set': {}}  # Using MongoDB's $set operator
    for field, new_value in data.items():
        if field != 'id':  # Prevent ID from being changed
            update_query['$set'][field] = new_value

    # 3. Perform the update
    rocrate_collection.update_one({'_id': rocrate['_id']}, update_query) 

    return jsonify({'message': 'RO-Crate updated'}), 200

@app.route('/rocrate/<rocrate_id>', methods=['DELETE'])
def delete_rocrate(rocrate_id):
    # 1. Find the RO-Crate
    rocrate = rocrate_collection.find_one({'id': rocrate_id})
    if not rocrate:
        return jsonify({'error': 'RO-Crate not found'}), 404

    # 2. Delete the RO-Crate
    rocrate_collection.delete_one({'id': rocrate_id})

    return jsonify({'message': 'RO-Crate deleted'}), 200

# ... Other FOCA setup code ...

if __name__ == '__main__':
    app.run(debug=True) 
