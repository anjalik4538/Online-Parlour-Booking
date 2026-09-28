# 💇‍♀️ Online Parlour Booking System

A full-stack web application for managing parlour services and online appointments. Users can browse available services, select a date and time, and book appointments online. An admin dashboard is provided to manage bookings and appointments.

## 🚀 Features

* User-friendly home page
* Browse parlour services
* Online appointment booking
* Date and time selection
* Booking confirmation
* Admin dashboard
* Manage customer bookings
* Responsive design
* REST API-based backend

## 🛠️ Technologies Used

### Frontend

* React.js
* JavaScript (ES6+)
* HTML5
* CSS3
* Axios

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite

### Tools

* Git
* GitHub
* VS Code

## 📂 Project Structure

```text
Online-Parlour-Booking/
│
├── backend-django/
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── booking/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   └── manage.py
│
├── frontend-react/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── README.md
│
└── .gitignore
```

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Online-Parlour-Booking.git
cd Online-Parlour-Booking
```

### 2. Run Backend

```bash
cd backend-django
python manage.py runserver
```

The Django backend will run on:

```text
http://127.0.0.1:8000/
```

### 3. Run Frontend

Open another terminal:

```bash
cd frontend-react
npm install
npm start
```

The React application will run on:

```text
http://localhost:3000/
```

## 🎯 Purpose

The main purpose of this project is to provide a convenient online platform for customers to explore parlour services and book appointments while allowing the admin to manage bookings efficiently.

## 🔮 Future Improvements

* Online payment integration
* User authentication and registration
* Email/SMS booking notifications
* Customer booking history
* Cloud database integration
* Deployment on cloud platforms

## 👩‍💻 Author

**Anjali Kumari**

B.Tech Computer Science Engineering (AI)
