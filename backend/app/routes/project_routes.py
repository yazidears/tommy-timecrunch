from flask import Blueprint, jsonify, request

projects = Blueprint('projects', __name__)

@projects.route('/', methods=['POST'])
def create_project():
    # Return mock project data with ID
    return jsonify({"project_id": 1, "status": "created", "name": "New Project"}), 201

@projects.route('/<int:id>', methods=['GET'])
def get_project(id):
    # Dummy data
    return jsonify({})

@projects.route('/<int:id>', methods=['PUT'])
def update_project(id):
    # Dummy data
    return jsonify({})

@projects.route('/<int:id>', methods=['DELETE'])
def delete_project(id):
    # Dummy data
    return jsonify({}), 204

@projects.route('/<int:id>/ship', methods=['POST'])
def ship_project(id):
    # Dummy data
    return jsonify({})

@projects.route('/<int:id>/ship', methods=['GET'])
def get_shipment_status(id):
    # Dummy data
    return jsonify({})
