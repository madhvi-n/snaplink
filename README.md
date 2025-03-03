# PyShortly - A URL Shortener

## 🚀 Overview
PyShortly is a simple yet powerful URL shortener built with **Python (Flask)** and **HTMX/React** for the frontend. It allows users to shorten long URLs, track visits, and even generate QR codes for quick access. The app is deployed on **Render** for seamless cloud hosting.

## ✨ Features
- 🔗 **URL Shortening** – Convert long URLs into short, easy-to-share links.
- 🎨 **Custom Short Links** – Users can choose custom aliases for their links.
- 📊 **Click Tracking** – See how many times a link has been accessed.
- ⏳ **Expiration Dates** – Set an expiry time for temporary links.
- 🖥 **API Support** – Shorten URLs programmatically via a REST API.
- 📸 **QR Code Generation** – Generate QR codes for each shortened URL.
- 🚀 **Fast & Lightweight** – Uses HTMX/React for a snappy frontend experience.

## 🛠 Tech Stack
### **Backend:**
- Python (**Flask**)
- SQLite/PostgreSQL (Database)
- Redis (Caching short URLs for performance)

### **Frontend:**
- **HTMX** (for lightweight dynamic UI) or **React** (for a more interactive experience)
- Tailwind CSS (for styling)

### **Deployment:**
- **Render** (for easy cloud hosting)
- Docker (optional, for containerized deployment)

## 📦 Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/pyshortly.git
cd pyshortly
```

### **2. Create a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Run the Application**
For Django:
```sh
python manage.py migrate
python manage.py runserver
```
For Flask:
```sh
flask run
```

### **4. Open in Browser**
Visit `http://127.0.0.1:8000/` to access the app.

## 📌 API Usage
### **Shorten a URL (POST /shorten)**
```sh
curl -X POST "https://yourdomain.com/shorten" -d "url=https://example.com"
```
Response:
```json
{
  "short_url": "https://shrinkr.ly/abc123"
}
```

Made with ❤️ using Python & HTMX/React.

