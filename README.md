# SnapLink - A URL Shortener

[![Django CI](https://github.com/madhvi-n/snaplink/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/madhvi-n/snaplink/actions/workflows/django.yml)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1-brightgreen?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/Django_Rest_Framework-3.15-red)](https://www.django-rest-framework.org/)
[![Angular](https://img.shields.io/badge/React-19-blueviolet)](https://react.dev/)

SnapLink is a simple yet powerful URL shortener built with **Python (Django)** and **React** for the frontend. It allows users to shorten long URLs, track visits, and even generate QR codes for quick access.

## ✨ Features

- 🔗 **URL Shortening** – Convert long URLs into short, easy-to-share links.
- 📊 **Click Tracking** – See how many times a link has been accessed.
- ⏳ **Expiration Dates** – Set an expiry time for temporary links.
- 📸 **QR Code Generation** – Generate QR codes for each shortened URL (To Do).
- 🚀 **Fast & Lightweight** – Uses HTMX/React for a snappy frontend experience (To Do).

## 🛠 Tech Stack

### **Backend:**

- Python (**Django**)
- SQLite/PostgreSQL (Database)
- Redis (Caching short URLs for performance)

### **Frontend:**

- React
- Tailwind CSS (for styling)

## 📦 Installation & Setup

1. Clone the Repository

    ```sh
    git clone https://github.com/madhvi-n/snaplink.git
    cd snaplink
    ```

2. Set up a virtual environment

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Apply Database Migrations

    ```bash
    python manage.py migrate
    ```

5. Create a Superuser

    ```bash
    python manage.py createsuperuser
    ```

6. Run the Development Server

    ```bash
    python manage.py runserver
    ```

    Access the application at: <http://127.0.0.1:8000>

## Frontend

1. Install dependencies

    ```bash
        npm install
    ```

2. Run the Development Server

    ```bash
        npm run dev
    ```

## 📝 API Documentation

The API documentation is available via **Swagger**:

- **Swagger UI:** `http://127.0.0.1:8000/api/swagger/`
- **Redoc:** `http://127.0.0.1:8000/api/redoc/`

## ⚙️ Environment Variables *(Example .env file)*

```ini
SECRET_KEY=django-secret-key
DEBUG=True
BASE_URL=http://localhost:8000
```

### 🎉 Happy Coding! 🚀
