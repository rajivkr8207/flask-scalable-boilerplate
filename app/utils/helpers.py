import re
import secrets
import string
from datetime import datetime, timezone
from werkzeug.utils import secure_filename


# Generate unique random string
def generate_random_string(length=12):

    characters = string.ascii_letters + string.digits

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )


# Generate unique token
def generate_token(length=32):

    return secrets.token_urlsafe(length)


# Get current UTC datetime
def get_current_datetime():

    return datetime.now(timezone.utc)


# Validate email
def is_valid_email(email):

    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    return bool(re.match(pattern, email or ""))


# Check empty value
def is_empty(value):

    return value is None or (
        isinstance(value, str) and not value.strip()
    )


# Sanitize filename
def sanitize_filename(filename):

    return secure_filename(filename)


# Convert string to slug
def generate_slug(text):

    text = text.lower().strip()

    text = re.sub(r"[^a-z0-9]+", "-", text)

    return text.strip("-")


# Get pagination values
def get_pagination(page=1, limit=10):

    page = max(1, int(page))
    limit = min(100, max(1, int(limit)))

    return {
        "page": page,
        "limit": limit,
        "offset": (page - 1) * limit
    }


# Convert datetime to ISO format
def format_datetime(value):

    if not value:
        return None

    return value.isoformat()


# Safe dictionary getter
def get_value(data, key, default=None):

    if not isinstance(data, dict):
        return default

    return data.get(key, default)