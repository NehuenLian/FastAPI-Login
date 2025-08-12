# FastAPI User Authentication System (REST API)

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)  
![FastAPI](https://img.shields.io/badge/fastapi-0.116.1-brightgreen.svg)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-2.0-blue.svg)

This project is a simple example of a user authentication system using **FastAPI** with a pure REST API (JSON only). It includes authentication with **JWT tokens**, **secure password hashing (bcrypt)**, **rate limiting**, role-based access control, and security features like **CORS** and HTTP headers.

---

## Features

* **User registration and login** with validation and secure password hashing.
* **JWT tokens with configurable expiration** for authorization.
* **Middleware to verify tokens** on each protected endpoint.
* **Role-based access control** for permission management.
* **Rate limiting** to prevent brute-force attacks.
* **CORS configuration** to accept requests only from trusted origins.
* **HTTP security headers** and HTTP → HTTPS redirection.
* **Global exception handlers** for common and custom error handling.

---

## Tech Stack

* **Python**
* **FastAPI**: Web framework for APIs.
* **Uvicorn**: ASGI server to run FastAPI apps.
* **SQLAlchemy**: ORM.
* **python-dotenv**: Environment variable management.
* **python-jose**: JWT creation and verification.
* **passlib + bcrypt**: Secure password hashing.
* **slowapi**: Rate limiting.
* **Pydantic**: Data validation.

---

## 📂 Structure

```
.
├── app/
│   ├── crud.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── data_access/
│   │   └── database.py
│   ├── routes/
│   │   └── auth.py
│   └── security/
│       ├── password_utils.py
│       └── tokens_utils.py
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to Run

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/NehuenLian/FastAPI-Login
    ```

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # Linux/macOS
    source .venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the server**:
    ```bash
    uvicorn app.main:app --reload
    ```
---

## Additional Notes

* **Database**: Defaults to SQLite, but you can configure any other database by changing the `DATABASE_URL`.
* **Authentication**: Tokens have configurable expiration time for improved security.
* **Roles**: Access control is based on roles, verified on each protected endpoint.
* **Rate limiting**: Helps protect against brute-force attacks by limiting requests per IP.
* **Security**: CORS, HTTP headers, and HTTPS redirection enhance API security.
