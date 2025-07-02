from flask import Blueprint, jsonify

inbox_bp = Blueprint('inbox_bp', __name__)

@inbox_bp.route('/', methods=['GET'])
def get_inbox():
    # Mock response
    return jsonify([])
