# 📚 Secure Book Management REST API

A RESTful API built using Django and Django REST Framework (DRF) for managing book records with secure authentication and user-based access control.

---

## 🚀 Features

- User Authentication using JWT (Access & Refresh Tokens)
- Secure Login System
- CRUD Operations (Create, Read, Update, Delete)
- User-specific data access (Custom Permissions)
- API Testing using Thunder Client
- role-based permissions
- search/filtering
- pagination
- file upload
- API documentation using Swagger

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- SQLite
- JWT Authentication

---

## 🔐 Authentication

This API uses **JWT (JSON Web Token)** authentication.

- After login, you will receive:
  - Access Token
  - Refresh Token

- Use the access token in headers:

Authorization: Bearer <your_access_token>


---

## ▶️ How to Run Locally

1. Clone the repository:
git clone https://github.com/yourusername/project


2. Navigate to project folder:
cd project


3. Create virtual environment:
python -m venv venv


4. Activate virtual environment:
- Windows:
venv\Scripts\activate


5. Install dependencies:
pip install -r requirements.txt


6. Run migrations:
python manage.py migrate


7. Start server:
python manage.py runserver


---

## 📸 API Testing

Use tools like:
- Thunder Client

---

## 👨‍💻 Author

Pratvi Jikadra
