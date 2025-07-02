from flask import Blueprint, request, jsonify

commit_devlog = Blueprint('commit_devlog', __name__)

@commit_devlog.route('/webhooks/wakatime', methods=['POST'])
def wakatime_webhook():
    # Dummy data
    return jsonify({}), 200

@commit_devlog.route('/participants/<int:id>/commits', methods=['GET'])
def get_commits(id):
    # Dummy data
    return jsonify([])

@commit_devlog.route('/participants/<int:id>/devlogs', methods=['GET'])
def get_devlogs(id):
    # Dummy data
    return jsonify([])

@commit_devlog.route('/participants/<int:id>/devlogs', methods=['POST'])
def create_devlog(id):
    # Dummy data
    return jsonify({}), 201
