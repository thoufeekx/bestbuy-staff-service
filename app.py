from flask import Flask, jsonify, request
from uuid import uuid4
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# In-memory staff data (example data)
staff_data = {
    "1": {
        "id": "1",
        "name": "John Doe",
        "position": "Sales Associate",
        "department": "Sales",
        "email": "john.doe@bestbuy.com",
        "phone": "123-456-7890"
    },
    "2": {
        "id": "2",
        "name": "Jane Smith",
        "position": "Customer Service Representative",
        "department": "Support",
        "email": "jane.smith@bestbuy.com",
        "phone": "987-654-3210"
    },
    "3": {
        "id": "3",
        "name": "Alice Johnson",
        "position": "Store Manager",
        "department": "Management",
        "email": "alice.johnson@bestbuy.com",
        "phone": "555-123-4567"
    }
}

# CRUD operations

# Create a staff member
@app.route('/staff', methods=['POST'])
def create_staff():
    staff = request.json
    staff_id = str(uuid4())
    staff['id'] = staff_id
    staff_data[staff_id] = staff
    return jsonify(staff), 201

# Read all staff members
@app.route('/staff', methods=['GET'])
def get_all_staff():
    return jsonify(list(staff_data.values())), 200

# Read a specific staff member
@app.route('/staff/<staff_id>', methods=['GET'])
def get_staff(staff_id):
    staff = staff_data.get(staff_id)
    if staff:
        return jsonify(staff), 200
    return jsonify({'error': 'Staff not found'}), 404

# Update a staff member
@app.route('/staff/<staff_id>', methods=['PUT'])
def update_staff(staff_id):
    if staff_id in staff_data:
        updated_staff = request.json
        updated_staff['id'] = staff_id
        staff_data[staff_id] = updated_staff
        return jsonify(updated_staff), 200
    return jsonify({'error': 'Staff not found'}), 404

# Delete a staff member
@app.route('/staff/<staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    if staff_id in staff_data:
        del staff_data[staff_id]
        return jsonify({'message': 'Staff deleted successfully'}), 200
    return jsonify({'error': 'Staff not found'}), 404

if __name__ == '__main__':
    # Get port from .env or default to 5000
    port = os.getenv('PORT', 5000)
    app.run(debug=True, port=int(port))
