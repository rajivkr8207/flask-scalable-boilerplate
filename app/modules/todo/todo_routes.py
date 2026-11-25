from flask import Blueprint

from app.modules.todo.todo_controller import (
    create_todo,
    get_all_todos,
    get_todo,
    update_todo,
    delete_todo,
    status_update
)


todo_bp = Blueprint(
    "todo",
    __name__
)


todo_bp.route("", methods=["POST"], strict_slashes=False)(create_todo)
todo_bp.route("", methods=["GET"], strict_slashes=False)(get_all_todos)
todo_bp.route("/<int:todo_id>", methods=["GET"])(get_todo)
todo_bp.route("/<int:todo_id>", methods=["PUT"])(update_todo)
todo_bp.route("/<int:todo_id>", methods=["DELETE"])(delete_todo)
todo_bp.route("/<int:todo_id>/status", methods=["PUT"])(status_update)