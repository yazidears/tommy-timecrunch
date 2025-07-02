from flask import Blueprint, jsonify, request

reports = Blueprint('reports', __name__)

@reports.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Dummy data
    return jsonify([])

@reports.route('/pdf', methods=['GET'])
def get_pdf_report():
    # Dummy data
    return "PDF Report", 200
