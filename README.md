<div align="center">

# ⚡ Flask REST API Boilerplate
### Production-Ready, Modular & Scalable RESTful API Architecture with Flask, SQLAlchemy & Marshmallow

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg?logo=flask)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-red.svg)](https://www.sqlalchemy.org/)
[![Marshmallow](https://img.shields.io/badge/Marshmallow-3.x%20%7C%204.x-purple.svg)](https://marshmallow.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A modern, highly-extensible **Flask REST API Boilerplate** built using clean layered architecture and domain-driven modular design. Designed for developers building enterprise-grade, high-performance web APIs and microservices.

[Features](#-key-features) • [Project Structure](#-project-structure) • [Quick Start](#-quick-start) • [Adding New Modules](#-how-to-create-a-new-module) • [Shared Services](#-shared-services) • [API Reference](#-api-endpoints)

</div>

---

## 🌟 Key Features

- **Modular Domain Architecture**: Isolated modules (`routes`, `controller`, `service`, `model`, `schemas`) for maintainability and scalability.
- **Layered Clean Architecture**: Strict separation of concerns (Routes $\rightarrow$ Controller $\rightarrow$ Service $\rightarrow$ Model).
- **Automated Validation & Serialization**: Robust schema validation and deserialization powered by **Marshmallow**.
- **Centralized Error Handling**: Global exception interceptor returning consistent, readable JSON error payloads.
- **Unified API Response Standard**: Standardized `{ success, message, data }` response wrapper across all endpoints.
- **SQLAlchemy with BaseModel**: Pre-configured abstract `BaseModel` featuring auto-incrementing `id`, UTC `created_at`, `updated_at`, and `is_deleted` soft-delete flags.
- **Environment-based Configuration**: 12-Factor App compliant configuration loaded via `.env` (`DevelopmentConfig`, `ProductionConfig`).
- **Cross-Cutting Shared Services**: Dedicated `services/` layer for reusable components (e.g., Mailer, Cloud Storage, Payment Gateways).

---

## 📁 Project Structure

```text
restfullapi/
├── app/
│   ├── config/             # App settings, environment variables & profiles
│   │   ├── config.py       # DevelopmentConfig, ProductionConfig, Base Config
│   │   └── init.py
│   ├── database/           # Database engine & base models
│   │   ├── baseModel.py    # Abstract model with id, timestamps & soft-delete
│   │   ├── db.py           # SQLAlchemy instance & DB initializer
│   │   └── __init__.py
│   ├── decorators/         # Custom decorators (auth guards, rate-limiting, permissions)
│   ├── exceptions/         # Centralized error handling
│   │   ├── custom_exceptions.py  # AppError, NotFoundError, ValidationError, etc.
│   │   ├── error_handler.py      # Global Flask error handlers (JSON output)
│   │   └── __init__.py
│   ├── modules/            # Domain-driven feature modules
│   │   └── todo/           # Example: Complete CRUD Todo Module
│   │       ├── todo_model.py       # SQLAlchemy ORM model
│   │       ├── todo_schemas.py     # Request/Response Marshmallow schemas
│   │       ├── todo_service.py     # Core business logic & database queries
│   │       ├── todo_controller.py  # HTTP request parsing & response delivery
│   │       ├── todo_routes.py      # Blueprint definition & route mapping
│   │       └── __init__.py         # Clean public exports
│   ├── services/           # Shared cross-cutting services (Mailer, S3, Payments)
│   │   └── .gitkeep
│   ├── utils/              # Reusable utilities
│   │   ├── api_response.py # Unified JSON response builder
│   │   ├── async_handler.py# Async execution helpers
│   │   └── helpers.py      # String, date & formatting utilities
│   ├── module_register.py  # Single source of truth for blueprint registration
│   └── __init__.py         # Application factory (Create_app)
├── .env.example            # Environment variables template
├── requirements.txt        # Production dependencies
└── run.py                  # Application launcher
```

---

## 🚀 Quick Start

### 1. Prerequisites
- Python `3.10+` installed
- `git` installed

### 2. Clone and Setup Environment

```bash
# Clone the repository
git clone https://github.com/rajivkr8207/flask-scalable-boilerplate.git
cd flask-scalable-boilerplate

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate || source .venv\Scripts\activate
# On macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create `.env` by copying `.env.example`:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Update your `.env`:
```env
SECRET_KEY=super-secret-key-change-this-in-production
DATABASE_URL=sqlite:///todo.db
DEBUG=True
```

### 5. Launch Development Server

```bash
python run.py
```

The API will be available at: **`http://127.0.0.1:5000`**

---

## 🧩 How to Create a New Module

Adding a new domain (e.g., `auth`, `users`, or `products`) is straightforward and modular.

### Step 1: Create the Module Directory
Create `app/modules/auth/` containing:
- `auth_model.py`
- `auth_schemas.py`
- `auth_service.py`
- `auth_controller.py`
- `auth_routes.py`
- `__init__.py`

### Step 2: Implement Components

#### Model (`app/modules/auth/auth_model.py`)
```python
from app.database import db, BaseModel

class User(BaseModel):
    __tablename__ = "users"

    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
```

#### Routes (`app/modules/auth/auth_routes.py`)
```python
from flask import Blueprint
from .auth_controller import register, login

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/register", methods=["POST"])(register)
auth_bp.route("/login", methods=["POST"])(login)
```

#### Public Exports (`app/modules/auth/__init__.py`)
```python
from .auth_routes import auth_bp
from .auth_model import User

__all__ = ["auth_bp", "User"]
```

### Step 3: Register in `module_register.py`
Add your new blueprint in [app/module_register.py](file:///d:/flask/restfullapi/app/module_register.py):

```python
from app.modules.todo import todo_bp
from app.modules.auth import auth_bp  # 1. Import blueprint

def Module_register(app):
    apiurl = "/api/v1"

    app.register_blueprint(todo_bp, url_prefix=f"{apiurl}/todos")
    app.register_blueprint(auth_bp, url_prefix=f"{apiurl}/auth")  # 2. Register with prefix
```

Your endpoints will now be live under `/api/v1/auth/register` and `/api/v1/auth/login`.

---

## ⚙️ Shared Services (`app/services/`)

Use `app/services/` for logic that needs to be consumed across **multiple modules**:

| Service Example | Purpose |
|---|---|
| `email_service.py` | Send welcome emails, password resets, OTPs via SMTP/SendGrid |
| `storage_service.py` | Upload & manage media files on AWS S3 or Cloudinary |
| `payment_service.py` | Handle payments, checkout sessions, and webhook verifications |
| `notification_service.py` | Dispatch SMS, Slack alerts, or mobile push notifications |

*Note: Business logic tied only to a single domain should remain inside its respective module (`app/modules/<module>/<module>_service.py`).*

---

## 📡 API Endpoints (Reference)

All endpoints follow the base route: `/api/v1/todos`

| Method | Endpoint | Description | Status Code |
|:---:|---|---|:---:|
| `GET` | `/api/v1/todos?page=1&limit=10` | Fetch paginated list of todos | `200 OK` |
| `POST` | `/api/v1/todos` | Create a new todo item | `201 Created` |
| `GET` | `/api/v1/todos/<id>` | Fetch single todo by ID | `200 OK` |
| `PUT` | `/api/v1/todos/<id>` | Update todo title, status, or priority | `200 OK` |
| `DELETE` | `/api/v1/todos/<id>` | Soft delete todo item | `200 OK` |

### Example Request (Create Todo)
```bash
curl -X POST http://127.0.0.1:5000/api/v1/todos \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete documentation",
    "description": "Write a clean README for the project",
    "priority": "high"
  }'
```

### Standard Response Format
```json
{
  "success": true,
  "message": "Todo created successfully",
  "data": {
    "id": 1,
    "title": "Complete documentation",
    "description": "Write a clean README for the project",
    "status": "pending",
    "priority": "high",
    "created_at": "2026-11-25T13:07:37.407740",
    "updated_at": "2026-11-25T13:07:37.407745"
  }
}
```

---

## 🛡️ Error Handling

Errors return a consistent structure with appropriate HTTP status codes:

```json
{
  "success": false,
  "message": "Validation failed",
  "data": {
    "title": ["Length must be between 3 and 150."]
  }
}
```

Supported out-of-the-box exceptions:
- `AppError` (`400`)
- `ValidationError` (`400`)
- `UnauthorizedError` (`401`)
- `NotFoundError` (`404`)
- Internal Server Error (`500`)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.
