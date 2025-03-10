# 🍽️ Mealmate - Food Ordering Web App 🚀

Mealmate is a powerful and user-friendly web application built with **Django**, designed to streamline online food ordering. This platform supports both **restaurant owners** and **customers**, enabling seamless management of restaurant listings, menus, orders, and payments via **Razorpay**. 🍔🍕🥗

---

## 🌟 Features & Functionalities

### 🔐 User Authentication & Management
✅ Secure **sign-up and login** for customers and restaurant owners  
✅ Authentication powered by **Django’s built-in security**  

### 🏪 Restaurant Management System
✅ **Owners can:**
- 🏗️ Add new restaurants  
- 🛠️ Edit & update restaurant details  
- 🗑️ Remove restaurants  

### 📜 Menu & Ordering System
✅ **Customers can:**
- 🍽️ Browse restaurant menus  
- 🛒 Add items to the cart  
- 📦 Place an order  

### 💳 Secure Payment Processing
✅ **Razorpay integration** for fast and secure transactions  
✅ Seamless payment flow for a hassle-free experience  

---

## ⚡ Quick Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/mealmate.git
cd mealmate
```

### 2️⃣ Set Up a Virtual Environment 🏗️
```sh
python3 -m venv env
source env/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies 📦
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations 🗄️
```sh
python manage.py migrate
```

### 5️⃣ Create an Admin User 🔑
```sh
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server 🚀
```sh
python manage.py runserver
```
🌐 **Access the app at:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

---

## 📂 Project Structure

```
mealmate/
│── core/
│   │── migrations/
│   │── static/
│   │── templates/core/
│   │   ├── 🏗️ restaurant_form.html
│   │   ├── 🎨 layout.html
│   │   ├── 💳 checkout_page.html
│   │   ├── 🍔 menu_display.html
│   │   ├── 🏠 user_dashboard.html
│   │   ├── 📜 restaurant_listings.html
│   │   ├── 🌎 homepage.html
│   │   ├── 🛍️ orders_view.html
│   │   ├── 🛒 shopping_cart.html
│   │   ├── 🔐 login_page.html
│   │   ├── 📝 registration.html
│   │   ├── ✅ payment_success.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── views.py
│── manage.py
│── requirements.txt
```

---

## 📡 API Endpoints (Django REST Framework)
| ⚡ Method | 🌍 Endpoint | 📌 Functionality |
|--------|--------------------------|---------------------------|
| GET | `/api/restaurants/` | Fetch all restaurants |
| POST | `/api/restaurants/create/` | Add a new restaurant |
| PUT | `/api/restaurants/edit/<id>/` | Modify restaurant details |
| DELETE | `/api/restaurants/remove/<id>/` | Delete a restaurant |
| GET | `/api/menu/` | Retrieve menu items |
| POST | `/api/order/` | Place an order |

---

## 💰 Razorpay Payment Integration
1️⃣ **Register on Razorpay** at [razorpay.com](https://razorpay.com)  
2️⃣ **Obtain API credentials** from the Razorpay dashboard  
3️⃣ **Update Django settings** with the API keys:  
```python
RAZORPAY_API_KEY = "your_api_key"
RAZORPAY_API_SECRET = "your_api_secret"
```
