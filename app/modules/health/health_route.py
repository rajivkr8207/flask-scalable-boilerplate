
from flask import Blueprint
from .health_controller import health_check 


health_bp = Blueprint(
    "health",
    __name__,
)


health_bp.route("", methods=["GET"],  strict_slashes=False)(health_check)
