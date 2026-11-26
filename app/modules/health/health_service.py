
from datetime import datetime, timezone
import time
import platform
from flask import current_app
APP_START_TIME = time.time()


class HealthService:
    @staticmethod
    def get_health_status():
        current_time = time.time()

        uptime_seconds = int(current_time - APP_START_TIME)

        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        uptime = f"{days}d {hours}h {minutes}m {seconds}s"

        return {
            "status": "healthy",
            "message": "Application is running successfully",

            "application": {
                "name": current_app.config.get("APPLICATION_NAME"),
                "environment": current_app.config.get("FLASK_ENV"),
                "version": "1.0.0",
                "debug": current_app.config.get("DEBUG")
            },

            "server": {
                "uptime_seconds": uptime_seconds,
                "uptime": uptime,
                "python_version": platform.python_version(),
                "platform": platform.system(),
                "hostname": platform.node()
            },

            "timestamp": datetime.now(
                timezone.utc
            ).isoformat(),

            "timezone": "UTC"
        }
