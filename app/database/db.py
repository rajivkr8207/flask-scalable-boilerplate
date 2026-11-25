from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config
from flask import current_app
db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config.get("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    
    with app.app_context():
        db.create_all()