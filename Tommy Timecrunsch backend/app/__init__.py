from flask import Flask
from config import config  # Ensure we import the dictionary 'config'
from .extensions import db, migrate, socketio, bcrypt, jwt
import os

def create_app(config_name=os.getenv('FLASK_CONFIG') or 'default'):
    app = Flask(__name__, instance_relative_config=True)
    # Use the config dictionary, not the Config class
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .routes.admin_routes import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/api/admin')

    from .routes.ai_npc_routes import ai_npc_bp
    app.register_blueprint(ai_npc_bp, url_prefix='/api')

    from .routes.commit_devlog_routes import commit_devlog
    app.register_blueprint(commit_devlog, url_prefix='/api')

    from .routes.game_routes import game_bp
    app.register_blueprint(game_bp, url_prefix='/api/game')

    from .routes.housing_routes import housing_bp
    app.register_blueprint(housing_bp, url_prefix='/api/housing')

    from .routes.inbox_routes import inbox_bp
    app.register_blueprint(inbox_bp, url_prefix='/api/inbox')

    from .routes.participant_routes import participants_bp
    app.register_blueprint(participants_bp, url_prefix='/api')

    from .routes.project_routes import projects
    app.register_blueprint(projects, url_prefix='/api/projects')

    from .routes.receipt_routes import receipt_bp
    app.register_blueprint(receipt_bp, url_prefix='/api/receipts')

    from .routes.report_routes import reports
    app.register_blueprint(reports, url_prefix='/api/reports')

    from .routes.stipend_flight_routes import stipend_flight
    app.register_blueprint(stipend_flight, url_prefix='/api')

    return app
