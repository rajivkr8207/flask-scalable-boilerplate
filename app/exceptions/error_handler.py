from flask import jsonify
from app.exceptions.custom_exceptions import AppError


def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(error):
        return jsonify({
            "success": False,
            "message": error.message,
            "data": None
        }), error.status_code

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({
            "success": False,
            "message": "Route not found",
            "data": None
        }), 404

    @app.errorhandler(500)
    def handle_internal_error(error):
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "data": None
        }), 500