# 🚀 Organization Management Backend (FastAPI + MongoDB)

A clean, modular, and scalable backend service for managing organizations and admin operations. Built using **FastAPI**, **Motor (MongoDB)**, and **JWT authentication**. This project follows modern backend engineering practices with a clear folder structure and reusable components.

---

## 🧩 Design Notes – Modular & Clean Architecture

The backend is designed using a **modular, layered architecture** to ensure maintainability, clarity, and future scalability. Each file and directory has **one dedicated responsibility**, enabling easy navigation and extension.

---

## 📁 Project Structure
app/
│── main.py               → FastAPI app initialization & router mounting
│── database.py           → MongoDB connection (Motor)
│── schemas.py            → Pydantic models for validation & serialization
│── utils.py              → Helper functions (password hashing, JWT tokens)
│── crud.py               → Database operations (create, update, query)
│── routes/
│     ├── org_routes.py   → Organization API endpoints
│     └── admin_routes.py → Admin authentication & management APIs
tests/                    → Unit & integration tests

---

## 🧠 Why Modular Design?

- Routes Layer — Handles request/response logic  
- CRUD Layer — Manages all database operations  
- Schemas Layer — Ensures strict input/output validation  
- Database Layer — MongoDB async connection using Motor  
- Utils Layer — Reusable utilities like hashing & token creation  
- Tests Layer — Supports unit and integration testing  

This structure keeps the codebase **clean, readable, testable, and scalable**.

---

## 🏗️ Core Design Principles

- Single Responsibility Principle  
- Separation of Concerns  
- Async-first performance (FastAPI + Motor)  
- Secure authentication (bcrypt + JWT)  
- Highly testable architecture  

---

## 🚀 Benefits

- Easy to maintain and extend  
- Clean and professional architecture  
- Reusable components  
- Scales effortlessly for future features  
- Ready for Docker deployment  

---

## 🚀 Instructions to Run the Application

### 1️⃣ Clone the repository
git clone https://github.com/surajdidwagh/org-mgmt-backend.git
cd org-mgmt-backend

### 2️⃣ Create & activate a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\Activate.ps1

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Start MongoDB
mongod --dbpath C:\data\db

### 5️⃣ Run FastAPI server
.\venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001

### 6️⃣ Access API Documentation
Swagger UI → http://127.0.0.1:8001/docs  
ReDoc → http://127.0.0.1:8001/redoc  

---

## 📌 Example API Call (PowerShell)
Invoke-RestMethod -Uri "http://127.0.0.1:8001/org/create" -Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{"organization_name":"DemoOrg","email":"demo@org.com","password":"DemoPass123"}'

---

## 🧪 Run Tests
pytest

---

## 🐳 Run with Docker (Optional)
docker build -t org-mgmt-backend .
docker run -p 8001:8001 org-mgmt-backend

---

## ⭐ If you like this project
Feel free to **star the repository** and contribute!
