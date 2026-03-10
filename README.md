# ☕ Cafe Order Management System

## 📌 Project Description
The Cafe Order Management System is a web-based application designed to streamline and automate the process of managing orders in a cafe. It allows staff to efficiently take customer orders, manage menu items, track order status, and improve overall service delivery.

This system helps reduce manual errors, improve order accuracy, and enhance customer satisfaction.

---
## ⚙️ Installation & Setup

1. **Clone the repository:**
   `git clone https://github.com/cubiwanjohi/Cafe_Order_Management_System`
2. **Create a virtual environment:**
   `python -m venv venv`
3. **Activate virtual environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. **Install dependencies:**
   `pip install django djangorestframework`
5. **Run Migrations:**
   `python manage.py migrate`
6. **Start the server:**
   `python manage.py runserver`

## 📡 API Documentation
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/categories/` | List all food categories |
| **GET** | `/api/menu/` | View the full active menu |
| **POST** | `/api/orders/` | Submit a new order |

# Features
- 🧾 Add and manage customer orders
- 📋 View and update order status (Pending, Preparing, Completed)
- 🍔 Manage menu items (Add, Edit, Delete)
- 💰 Automatic total price calculation
- 👩‍🍳 Admin dashboard for managing operations
- 📊 Order history tracking
- 🔐 User authentication (Admin/Staff login)

---

## 🛠️ Technologies Used

- Frontend: HTML, CSS
- Backend: Django 
- Database: SQLite
- Version Control: Git & GitHub

---

## 📂 Project Structure
Cafe_Order_Management_System/
├── / luxz_cafe            # Project settings & main URL dispatcher
├── cafe/                 # Main App: Models, Views, Serializers
│   ├── migrations/       # Database version history
│   ├── serializers.py    # API Data translators
│   └── forms.py          # Web-based input validation
├── templates/            # HTML Frontend (home.html, register.html)
├── media/                # Uploaded menu item images
└── manage.py             # Django command-line utility
