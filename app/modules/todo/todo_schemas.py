from marshmallow import Schema, fields, validate, EXCLUDE


class CreateTodoSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    title = fields.String(
        required=True,
        validate=validate.Length(min=3, max=150)
    )
    description = fields.String(allow_none=True)
    status = fields.String(
        load_default="pending",
        validate=validate.OneOf([
            "pending",
            "in_progress",
            "completed"
        ])
    )
    priority = fields.String(
        load_default="medium",
        validate=validate.OneOf([
            "low",
            "medium",
            "high"
        ])
    )


class UpdateTodoSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    title = fields.String(
        validate=validate.Length(min=3, max=150)
    )

    description = fields.String(allow_none=True)

    status = fields.String(
        validate=validate.OneOf([
            "pending",
            "in_progress",
            "completed"
        ])
    )

    priority = fields.String(
        validate=validate.OneOf([
            "low",
            "medium",
            "high"
        ])
    )


class TodoResponseSchema(Schema):

    id = fields.Integer()
    title = fields.String()
    description = fields.String(allow_none=True)
    status = fields.String()
    priority = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
