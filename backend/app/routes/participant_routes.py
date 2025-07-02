from flask import Blueprint, jsonify, request

participants_bp = Blueprint('participants_bp', __name__)

@participants_bp.route('/hackathons/<int:id>/participants', methods=['GET'])
def get_hackathon_participants(id):
    # Mock response
    return jsonify([])

@participants_bp.route('/hackathons/<int:id>/participants', methods=['POST'])
def create_hackathon_participant(id):
    # Mock response with participant data
    return jsonify({
        "participant": {
            "id": 1,
            "hackathon_id": id,
            "name": "New Participant",
            "email": "participant@example.com",
            "github_username": "newbie",
            "skills": ["python", "flask"]
        }
    }), 201

@participants_bp.route('/participants/<int:id>', methods=['GET'])
def get_participant(id):
    # Mock response
    return jsonify({})

@participants_bp.route('/participants/<int:id>', methods=['PUT'])
def update_participant(id):
    # Mock response
    return jsonify({})

@participants_bp.route('/participants/<int:id>', methods=['DELETE'])
def delete_participant(id):
    # Mock response
    return jsonify({}), 204

@participants_bp.route('/participants/<int:id>/receipts', methods=['GET'])
def get_participant_receipts(id):
    # Mock receipt data
    return jsonify([])
