from flask import Flask
from .exceptions import register_error_handlers
from app.database import init_db
from app.config.init import Config
from .module_register import Module_register

def Create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    register_error_handlers(app)
    Module_register(app)

    return app
