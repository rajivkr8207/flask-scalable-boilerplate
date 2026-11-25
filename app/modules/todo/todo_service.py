from app.database import db
from app.modules.todo import Todo
from app.exceptions import NotFoundError, ValidationError


def create_todo(data):
    todo = Todo(**data)

    try:
        db.session.add(todo)
        db.session.commit()
        return todo
    except Exception:
        db.session.rollback()
        raise


def get_all_todos(page=1, limit=10):
    query = Todo.query.filter_by(is_deleted=False)

    total = query.count()

    todos = (
        query
        .order_by(Todo.created_at.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return {
        "todos": todos,
        "total": total,
        "page": page,
        "limit": limit
    }


def get_todo_by_id(todo_id):
    todo = Todo.query.filter_by(
        id=todo_id,
        is_deleted=False
    ).first()

    if not todo:
        raise NotFoundError("Todo not found")

    return todo


def update_todo(todo_id, data):
    if not data:
        raise ValidationError("No update data provided")

    todo = get_todo_by_id(todo_id)

    try:
        for key, value in data.items():
            setattr(todo, key, value)

        db.session.commit()
        return todo
    except Exception:
        db.session.rollback()
        raise


def delete_todo(todo_id):
    todo = get_todo_by_id(todo_id)

    try:
        todo.is_deleted = True
        db.session.commit()
        return True
    except Exception:
        db.session.rollback()
        raise
