from flask import Blueprint, jsonify, request

housing_bp = Blueprint('housing_bp', __name__)

@housing_bp.route('/listings', methods=['GET'])
def get_housing_listings():
    # Mock response
    return jsonify([])

@housing_bp.route('/apply', methods=['POST'])
def apply_for_housing():
    # Return mock application data with ID
    return jsonify({"application_id": 1, "status": "pending"}), 201

@housing_bp.route('/applications/<int:id>', methods=['GET'])
def get_application(id):
    # Dummy data
    return jsonify({})

@housing_bp.route('/applications/<int:id>', methods=['PUT'])
def update_application(id):
    # Dummy data
    return jsonify({})

# ... other housing routes ...
