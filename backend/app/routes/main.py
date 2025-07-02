from flask import Blueprint, request, jsonify
from ..extensions import db, bcrypt
from ..models import User, SaveData
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main = Blueprint('main', __name__)

@main.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if user already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"message": "User with this email already exists"}), 400
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], username=data['username'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        "user_id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "created_at": new_user.created_at.isoformat() if new_user.created_at else None
    }), 201

@main.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({
            "token": access_token,
            "user_id": user.id,
            "username": user.username,
            "expires_at": None  # JWT expiry would need to be calculated separately
        })
    return jsonify({"message": "Invalid credentials"}), 401

@main.route('/api/me', methods=['GET'])
@jwt_required()
def me():
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    return jsonify({"username": user.username, "email": user.email})

@main.route('/api/logout', methods=['POST'])
def logout():
    # In a real app, you'd handle token blacklisting
    return jsonify({"message": "Logged out"})

@main.route('/savedata/<int:user_id>', methods=['POST'])
@jwt_required()
def save_data(user_id):
    current_user_id = get_jwt_identity()
    if int(current_user_id) != user_id:
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.get_json()
    save = SaveData.query.filter_by(user_id=user_id).first()
    if save:
        save.data = data
    else:
        save = SaveData(user_id=user_id, data=data)
        db.session.add(save)
    db.session.commit()
    return jsonify({"message": "Data saved"})

@main.route('/data/<int:user_id>', methods=['GET'])
@jwt_required()
def get_data(user_id):
    current_user_id = get_jwt_identity()
    if int(current_user_id) != user_id:
        return jsonify({"message": "Unauthorized"}), 403

    save = SaveData.query.filter_by(user_id=user_id).first()
    if save:
        return jsonify(save.data)
    return jsonify({}), 404

@main.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Mock leaderboard data
    return jsonify([
        {"rank": 1, "username": "player1", "score": 1000},
        {"rank": 2, "username": "player2", "score": 900},
        {"rank": 3, "username": "player3", "score": 800}
    ])

@main.route('/')
def index():
    return "Hello, World!"
