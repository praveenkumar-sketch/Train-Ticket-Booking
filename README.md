# 🚆 Railway Ticket Booking System

A simple Railway Ticket Booking Web Application built using **Django (Python)**.
Users can signup, login, search trains, and book tickets.

---

## 📌 Features

* 🔐 User Authentication (Signup & Login)
* 🔍 Train Search (Source → Destination)
* 🚆 View Available Trains
* 🎟️ Ticket Booking
* 📉 Seat Availability Management
* ❌ Shows "Full" when no seats available

---

## 🛠️ Technologies Used

* Python 🐍
* Django 🌐
* HTML, CSS, Bootstrap 🎨
* SQLite (Database) 🗄️

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/railway-booking.git
cd railway-booking
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run server

```bash
python manage.py runserver
```

---

## 🌐 Usage

1. Open browser → `http://127.0.0.1:8000/`
2. Signup / Login
3. Search trains (From → To)
4. Click **Book**
5. Confirm ticket

---

## 📂 Project Structure

```
railway_project/
│── booking/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│── templates/
│   ├── login.html
│   ├── signup.html
│   ├── search.html
│   ├── booking.html
│── db.sqlite3
│── manage.py
```

---

## 🚀 Future Improvements

* 📄 Booking history
* 🎫 Ticket ID generation
* 💳 Payment integration
* 📥 PDF ticket download
* 📱 Responsive UI enhancements

---

## 👨‍💻 Author

**Praveen Kumar**

---

## ⭐ Contribute

Feel free to fork this repo and improve the project!
