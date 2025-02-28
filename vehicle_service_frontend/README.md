# Vehicle Service Management System

## Project Overview

The Vehicle Service Management System is a **full-stack web application** built using **React.js (Frontend)** and **Django (Backend)** with **PostgreSQL/SQLite** as the database. It provides functionalities for managing vehicle repairs, tracking components, calculating service prices, and visualizing revenue with graphs.

---

## Tech Stack

- **Frontend:** React.js
- **Backend:** Django & Django REST Framework
- **Database:** PostgreSQL (or SQLite for development)
- **Charts Library:** Recharts (for revenue visualization)

---

## Prerequisites

Ensure you have the following installed on your system:

1. **Node.js & npm** (for frontend)
   - Download from: [https://nodejs.org/](https://nodejs.org/)
2. **Python 3 & pip** (for backend)
   - Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
3. **PostgreSQL (Optional, or use SQLite)**
   - Download from: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
4. **Git (for version control)**
   - Download from: [https://git-scm.com/](https://git-scm.com/)

---

## 🚀 Backend Setup (Django API)

### 1. Clone the Repository

```sh
git clone https://github.com/your-repository/vehicle-service-management.git
cd vehicle-service-management/backend
```

### 2. Create & Activate Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure Database

By default, SQLite is used. To use **PostgreSQL**, update `backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations & Create Superuser

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the Server

```sh
python manage.py runserver
```

Your Django API will be running at: **[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)**

---

## 🎨 Frontend Setup (React.js)

### 1. Navigate to Frontend Directory

```sh
cd ../frontend
```

### 2. Install Dependencies

```sh
npm install
```

### 3. Configure API URL (If Needed)

In `frontend/src/api.js`, ensure the correct backend URL is used:

```javascript
const API_URL = "http://127.0.0.1:8000/api/";
```

### 4. Start the React App

```sh
npm start
```

Your React frontend will be running at: **[http://localhost:3000/](http://localhost:3000/)**

---

## 🎯 Features Implemented

✔ Register vehicle components & pricing
✔ Track vehicle repairs & issues
✔ Calculate repair/service pricing
✔ Simulate payment processing
✔ Revenue graphs (daily, monthly, yearly)

---

## 🛠️ API Endpoints

| Endpoint           | Method   | Description                       |
| ------------------ | -------- | --------------------------------- |
| `/api/components/` | GET/POST | Retrieve or add components        |
| `/api/vehicles/`   | GET/POST | Retrieve or register vehicles     |
| `/api/repairs/`    | GET/POST | Retrieve or create repair records |

---

## 📸 Demonstration Screenshots

(Add images or video link here showing UI and functionality)

---

## 🤝 Contribution

Feel free to submit a pull request or open issues for improvements.

---

## 📜 License

This project is **MIT Licensed**. Use freely and contribute to its development!

---

## 📩 Contact

For any queries or support, reach out at **dhanush777.com\@gmail.com**.

