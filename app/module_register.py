from app.modules.todo import todo_bp
from app.modules.health import health_bp

def Module_register(app):
    urlprefix = "/api/v1"
    app.register_blueprint(todo_bp, url_prefix=f"{urlprefix}/todos")
    app.register_blueprint(health_bp, url_prefix=f"{urlprefix}/health")
