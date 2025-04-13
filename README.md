# 📝 ToDo WebApp 📌

A simple and efficient **To-Do List Web Application** built with Django. Easily manage your tasks with features like authentication, CRUD operations, task categorization, and completion tracking.

## 🚀 Features  
- ✅ **User Authentication** (Login/Signup)  
- ✅ **Create, Read, Update, Delete (CRUD) Tasks**  
- ✅ **Mark Tasks as Completed**  
- ✅ **Task Categories & Due Dates**  
- ✅ **Responsive UI**  

## 🛠 Tech Stack  
- **Backend:** Django, SQLite  
- **Frontend:** HTML, CSS  

## 📂 Setup & Installation  

### 1️⃣ Clone the Repository  
Run the following command to clone the project:  
```sh
git clone https://github.com/ayush-r-nair/TODO-WebApp.git
cd TODO-WebApp
```

### 2️⃣ Create & Activate Virtual Environment (Optional but Recommended)  
```sh
# For Windows:
python -m venv venv
venv\Scripts\activate

# For macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies  
Make sure you have `requirements.txt` in the project folder and install dependencies:  
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations  
```sh
python manage.py migrate
```

### 5️⃣ Run the Server  
```sh
python manage.py runserver
```

### 6️⃣ Open in Browser  
```
http://127.0.0.1:8000/
```

---

## 📜 Requirements  
This project requires:  
- Python 3.x  
- Django 5.1+  
- Pillow (for image processing)  

All dependencies are listed in **`requirements.txt`**.  
To install them, run:  
```sh
pip install -r requirements.txt
```
---

## 📂 File Structure  
```
ToDo-WebApp/
│── tasks/                  # App for task management
│── users/                  # App for user authentication
│── templates/              # HTML templates
│── static/                 # Static files (CSS, JS)
│── db.sqlite3              # Database file
│── manage.py               # Django management script
│── requirements.txt        # Required dependencies
│── README.md               # Documentation
```

---

