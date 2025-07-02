from flask import Blueprint, request, jsonify
import requests

ai_npc_bp = Blueprint('ai_npc_bp', __name__)

@ai_npc_bp.route('/ai/chat', methods=['POST'])
def ai_chat():
    data = request.get_json()
    response = requests.post("https://ai.hackclub.com/chat/completions", json=data)
    return jsonify(response.json()), response.status_code

@ai_npc_bp.route('/ai/model', methods=['GET'])
def get_model():
    try:
        response = requests.get("https://ai.hackclub.com/model")
        return jsonify(response.json()), response.status_code
    except:
        # Fallback if external API is down
        return jsonify({"model": "meta-llama/llama-4-maverick-17b-128e-instruct", "status": "available"}), 200

@ai_npc_bp.route('/npcs', methods=['GET'])
def get_npcs():
    # Dummy data
    return jsonify([])

@ai_npc_bp.route('/npc/<int:id>/chat', methods=['POST'])
def npc_chat(id):
    # Dummy data
    return jsonify({}), 201

# ... other AI/NPC routes ...
