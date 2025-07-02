from flask import Blueprint, jsonify, request

receipt_bp = Blueprint('receipt_bp', __name__)

@receipt_bp.route('/', methods=['POST'])
def upload_receipt():
    # Handle both JSON and form data
    # Return mock receipt data with ID
    return jsonify({"receipt_id": 1, "status": "uploaded"}), 201

@receipt_bp.route('/<int:id>', methods=['GET'])
def get_receipt(id):
    # Dummy data
    return jsonify({})

@receipt_bp.route('/participants/<int:id>/receipts', methods=['GET'])
def get_participant_receipts(id):
    # Dummy data
    return jsonify([])
