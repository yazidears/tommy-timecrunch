from flask import Blueprint, jsonify, request

stipend_flight = Blueprint('stipend_flight', __name__)

@stipend_flight.route('/stipends/request', methods=['POST'])
def request_stipend():
    # Dummy data
    return jsonify({}), 201

@stipend_flight.route('/stipends/<int:id>', methods=['GET'])
def get_stipend(id):
    # Dummy data
    return jsonify({})

@stipend_flight.route('/stipends/<int:id>/approve', methods=['PUT'])
def approve_stipend(id):
    # Dummy data
    return jsonify({})

@stipend_flight.route('/flights/request', methods=['POST'])
def request_flight():
    # Dummy data
    return jsonify({}), 201

@stipend_flight.route('/flights/<int:id>', methods=['GET'])
def get_flight(id):
    # Dummy data
    return jsonify({})
