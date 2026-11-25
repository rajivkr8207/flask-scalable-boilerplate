from flask import request
from marshmallow import ValidationError as SchemaError

from app.modules.todo.todo_service import (
    create_todo as create_todo_service,
    get_all_todos as get_all_todos_service,
    get_todo_by_id as get_todo_service,
    update_todo as update_todo_service,
    delete_todo as delete_todo_service
)

from app.modules.todo.todo_schemas import (
    CreateTodoSchema,
    UpdateTodoSchema,
    TodoResponseSchema
)

from app.utils import api_response


create_schema = CreateTodoSchema()
update_schema = UpdateTodoSchema()
todo_schema = TodoResponseSchema()


# CREATE TODO
def create_todo():
    try:
        payload = request.get_json(silent=True) or {}
        data = create_schema.load(payload)

        todo = create_todo_service(data)

        return api_response(
            success=True,
            message="Todo created successfully",
            data=todo_schema.dump(todo),
            status_code=201
        )

    except SchemaError as error:
        return api_response(
            success=False,
            message="Validation failed",
            data=error.messages,
            status_code=400
        )


# GET ALL TODOS
def get_all_todos():
    page = max(1, request.args.get("page", 1, type=int))
    limit = min(100, max(1, request.args.get("limit", 10, type=int)))

    result = get_all_todos_service(page, limit)

    return api_response(
        success=True,
        message="Todos fetched successfully",
        data={
            "todos": todo_schema.dump(
                result["todos"], many=True
            ),
            "total": result["total"],
            "page": page,
            "limit": limit
        }
    )


# GET SINGLE TODO
def get_todo(todo_id):
    todo = get_todo_service(todo_id)

    return api_response(
        success=True,
        message="Todo fetched successfully",
        data=todo_schema.dump(todo)
    )


# UPDATE TODO
def update_todo(todo_id):
    try:
        payload = request.get_json(silent=True) or {}
        data = update_schema.load(payload)

        if not data:
            return api_response(
                success=False,
                message="No update data provided",
                data=None,
                status_code=400
            )

        todo = update_todo_service(todo_id, data)

        return api_response(
            success=True,
            message="Todo updated successfully",
            data=todo_schema.dump(todo)
        )

    except SchemaError as error:
        return api_response(
            success=False,
            message="Validation failed",
            data=error.messages,
            status_code=400
        )


# UPDATE TODO STATUS
def status_update(todo_id):
    try:
        payload = request.get_json(silent=True) or {}
        data = update_schema.load(payload)

        if not data:
            return api_response(
                success=False,
                message="No update data provided",
                data=None,
                status_code=400
            )

        todo = update_todo_service(todo_id, data)

        return api_response(
            success=True,
            message="Todo updated successfully",
            data=todo_schema.dump(todo)
        )

    except SchemaError as error:
        return api_response(
            success=False,
            message="Validation failed",
            data=error.messages,
            status_code=400
        )

# DELETE TODO
def delete_todo(todo_id):
    delete_todo_service(todo_id)

    return api_response(
        success=True,
        message="Todo deleted successfully",
        data=None
    )
