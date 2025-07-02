from flask import Blueprint, jsonify, request

game_bp = Blueprint('game_bp', __name__)

@game_bp.route('/state', methods=['GET'])
def get_game_state():
    # Mock response for now
    return jsonify({
        'tick': 19283,
        'time_remaining': 120,
        'stress_level': 50,
        'budget_used': 25000,
        'budget_total': 100000,
        'reputation': 85,
        'active_events': [],
        'pending_actions': []
    })

@game_bp.route('/action', methods=['POST'])
def game_action():
    # Dummy data
    return jsonify({}), 200

@game_bp.route('/save', methods=['POST'])
def save_game():
    # Dummy data
    return jsonify({}), 200

@game_bp.route('/events/random', methods=['GET'])
def random_event():
    # Dummy data
    return jsonify({})