from datetime import datetime, timezone
from app.database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    is_deleted = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )