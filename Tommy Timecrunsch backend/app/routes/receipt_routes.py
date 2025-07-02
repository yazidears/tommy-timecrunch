from flask import Blueprint, jsonify, request

receipt_bp = Blueprint('receipt_bp', __name__)

@receipt_bp.route('/api/receipts', methods=['POST'])
def upload_receipt():
    # Dummy data
    return jsonify({}), 201

@receipt_bp.route('/api/receipts/<int:id>', methods=['GET'])
def get_receipt(id):
    # Dummy data
    return jsonify({})

@receipt_bp.route('/api/participants/<int:id>/receipts', methods=['GET'])
def get_participant_receipts(id):
    # Dummy data
    return jsonify([])
