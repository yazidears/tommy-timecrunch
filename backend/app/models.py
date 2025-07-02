from .extensions import db, bcrypt
from sqlalchemy.sql import func
import json
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    game_state = db.Column(db.Text, default='{}')
    stress_level = db.Column(db.Integer, default=0)
    budget = db.Column(db.Float, default=100000.0)
    reputation = db.Column(db.Integer, default=100)
    current_tick = db.Column(db.Integer, default=0)
    saved_data = db.relationship('SaveData', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def get_game_state(self):
        return json.loads(self.game_state)

    def set_game_state(self, state):
        self.game_state = json.dumps(state)

class SaveData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.Column(db.JSON, nullable=False)
    last_saved = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    github_username = db.Column(db.String(100))
    status = db.Column(db.String(50), default='pending')
    stress_level = db.Column(db.Integer, default=0)
    commit_count = db.Column(db.Integer, default=0)
    devlog_count = db.Column(db.Integer, default=0)
    housing_status = db.Column(db.String(50), default='unhoused')
    housing_id = db.Column(db.Integer, db.ForeignKey('housing.id'))
    stipend_amount = db.Column(db.Float, default=0.0)
    flight_status = db.Column(db.String(50), default='not_booked')
    last_active = db.Column(db.DateTime(timezone=True), server_default=func.now())
    hackathon_id = db.Column(db.Integer, db.ForeignKey('hackathon.id'))

class Hackathon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))
    participants = db.relationship('Participant', backref='hackathon', lazy=True)

class Housing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    capacity = db.Column(db.Integer, default=1)
    occupied_spots = db.Column(db.Integer, default=0)
    lease_expiry = db.Column(db.DateTime(timezone=True))
    price_per_night = db.Column(db.Float)
    location = db.Column(db.String(200))
    participants = db.relationship('Participant', backref='housing', lazy=True)

class Commit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    repository = db.Column(db.String(200))
    lines_added = db.Column(db.Integer)
    lines_removed = db.Column(db.Integer)

class Devlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    word_count = db.Column(db.Integer)
    sentiment = db.Column(db.String(50))

class Stipend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    amount = db.Column(db.Float)
    justification = db.Column(db.Text)
    receipt_urls = db.Column(db.Text)
    status = db.Column(db.String(50), default='pending')
    approved_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    approved_at = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    departure_city = db.Column(db.String(100))
    arrival_city = db.Column(db.String(100))
    departure_date = db.Column(db.DateTime(timezone=True))
    return_date = db.Column(db.DateTime(timezone=True))
    estimated_cost = db.Column(db.Float)
    actual_cost = db.Column(db.Float)
    status = db.Column(db.String(50), default='pending')
    booking_reference = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    filename = db.Column(db.String(200))
    category = db.Column(db.String(100))
    amount = db.Column(db.Float)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='pending')
    ai_validation = db.Column(db.String(50))
    flagged_reason = db.Column(db.Text)
    uploaded_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    repository_url = db.Column(db.String(200))
    status = db.Column(db.String(50), default='in_progress')
    completion_percentage = db.Column(db.Integer, default=0)
    last_commit = db.Column(db.DateTime(timezone=True))
    shipping_status = db.Column(db.String(50), default='not_shipped')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(100))
    personality = db.Column(db.Text)
    last_interaction = db.Column(db.DateTime(timezone=True))
    memory_count = db.Column(db.Integer, default=0)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_name = db.Column(db.String(100))
    from_email = db.Column(db.String(120))
    subject = db.Column(db.String(200))
    content = db.Column(db.Text)
    priority = db.Column(db.String(50))
    read_status = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    category = db.Column(db.String(100))

class GameEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(100))
    description = db.Column(db.Text)
    severity = db.Column(db.String(50))
    scheduled_at = db.Column(db.DateTime(timezone=True))
    executed_at = db.Column(db.DateTime(timezone=True))
    participants_affected = db.Column(db.Text) # JSON list of participant IDs
