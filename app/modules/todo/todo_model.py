from app.database import db
from app.database import BaseModel


class Todo(BaseModel):
    __tablename__ = "todos"

    title = db.Column(
        db.String(150),
        nullable=False
    )
    description = db.Column(
        db.Text,
        nullable=True
    )
    status = db.Column(
        db.String(30),
        default="pending",
        nullable=False
    )
    priority = db.Column(
        db.String(20),
        default="medium",
        nullable=False
    )
