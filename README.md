# 🏏 IPL Django Multi-App Project

This is a Django practice project demonstrating multi-app architecture using separate URL configurations for different IPL teams.

The project includes apps for:

- CSK
- MI
- RCB

Each app has its own:
- views.py
- urls.py
- app namespace

---

## 📁 Project Structure

IPL/
│
├── csk/
│   ├── views.py
│   ├── urls.py
│
├── mi/
│   ├── views.py
│   ├── urls.py
│
├── rcb/
│   ├── views.py
│   ├── urls.py
│
├── ipl/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py

---

## 🔗 URL Routing Structure

### Project Level (ipl/urls.py)

- /csk/ → includes csk.urls
- /mi/ → includes mi.urls
- /rcb/ → includes rcb.urls

### Example Routes

- /mi/captain/
- /mi/vicecaptain/
- /rcb/captain/
- /rcb/vicecaptain/

Each route returns an HttpResponse displaying team leadership information.

---

## 🛠️ Technologies Used

- Python 3.10
- Django
- VS Code
- Virtual Environment (venv)

---

## ▶️ How to Run

1. Clone the repository
2. Activate virtual environment
3. Install Django:

```bash
pip install django
```

4. Run server:

```bash
python manage.py runserver
```

5. Open in browser:

```
http://127.0.0.1:8000/mi/captain/
http://127.0.0.1:8000/rcb/vicecaptain/
```

---

## 🎯 Learning Objectives

This project was built to practice:

- Django multi-app architecture
- Using include() for modular routing
- App-level URL configuration
- Namespacing with app_name
- Clean project structure

---

## 👨‍💻 Author

Gautam Panda  
Aspiring Full Stack Developer  
