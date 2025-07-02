from flask import Blueprint, request, jsonify

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/events', methods=['GET'])
def get_admin_events():
    # Mock response
    return jsonify([])

@admin_bp.route('/events', methods=['POST'])
def create_admin_event():
    # Mock response
    return jsonify({}), 201

@admin_bp.route('/events/<int:id>', methods=['DELETE'])
def delete_admin_event(id):
    # Mock response
    return jsonify({}), 204

# ... other admin routes ...
