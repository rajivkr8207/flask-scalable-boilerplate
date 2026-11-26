
from .health_service import HealthService
from app.utils import api_response


def health_check():
    health_data = HealthService.get_health_status()
    return api_response(
        success=True,
        message="server is Healthy",
        data=health_data,
        status_code=200
    )
