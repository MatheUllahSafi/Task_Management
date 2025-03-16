# Task Management System

## 📌 Overview
The **Task Management System** is a web-based application built with **Django** that helps teams efficiently manage tasks with **role-based access control (RBAC)**. The system allows **Super Admins, Admins, and Users** to interact with tasks based on their permissions.

## 🚀 Features
### ✅ **Role-Based Access Control (RBAC)**
- **Super Admin**: Can **create, read, update, delete** tasks and manage users.
- **Admin**: Can **create, read, update, delete** tasks.
- **User**: Can **only view assigned tasks**.

### ✅ **Task Management**
- Create, update, and delete tasks (Admins & Super Admins).
- Assign tasks to specific users.
- Set task **status** (`TODO`, `In Progress`, `Blocked`, `Done`).
- Set task **priority** (`High`, `Medium`, `Low`).
- Maintain **task logs** to track updates.

### ✅ **Authentication & Security**
- User authentication with **Django’s built-in authentication system**.
- Password hashing for security.
- **Permissions enforcement** in views and templates.

### ✅ **Logging & Audit Trails**
- All task updates are logged to maintain an **audit trail**.
- Tracks **who updated the task, when, and what changed**.

### ✅ **Automated Deployment with CI/CD**
- Uses **GitHub Actions** for testing & deployment.
- Deployed using **PythonAnywhere**.

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/MatheUllahSafi/Task_Management.git
cd task-management
```

### **2️⃣ Create & Activate a Virtual Environment**
```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create a Super Admin User**
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### **6️⃣ Start the Development Server**
```bash
python manage.py runserver
```

Visit **`http://127.0.0.1:8000/`** in your browser.

---

## 🎨 UI Screenshots
![Task List](screenshots/task_list.png)
![Edit Task](screenshots/edit_task.png)
![User Permissions](screenshots/user_permissions.png)

---

## 📂 Project Structure
```
├── task_management/        # Django project directory
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # Web server entry point
│   ├── asgi.py            # Async entry point
│
├── tasks/                 # Task Management app
│   ├── migrations/       # Database migrations
│   ├── models.py         # Database models
│   ├── views.py          # Application logic
│   ├── urls.py           # Task app URLs
│   ├── templates/        # HTML templates
│
├── static/                # CSS, JS, images
├── templates/             # Global templates
├── manage.py              # Django management tool
└── requirements.txt        # Python dependencies
```

---

## 🔧 Environment Variables
Create a `.env` file and set the following:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
DATABASE_URL=sqlite:///db.sqlite3
```
Load environment variables before running the project:
```bash
source .env
```

---

## 🚀 Deployment
### **Deploying on PythonAnywhere**
```bash
git pull origin main
python manage.py migrate
python manage.py collectstatic --noinput
```
Reload the PythonAnywhere web app to apply changes.

### **Deploying on Render**
1. Push code to **GitHub**.
2. Set up **Render** and connect the repository.
3. Deploy the app using Render’s free-tier plan.

---

## 🔍 Troubleshooting
### **1️⃣ Database Issues (`no such table: auth_user`)**
```bash
python manage.py migrate
```

### **2️⃣ Virtual Environment Not Found**
Activate it manually:
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### **3️⃣ Collectstatic Not Working**
Ensure `whitenoise` is installed and run:
```bash
python manage.py collectstatic --noinput
```

---

## 👨‍💻 Contributing
1. **Fork the repository**.
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Commit changes**: `git commit -m "Added feature X"`
4. **Push to GitHub**: `git push origin feature-name`
5. **Submit a pull request** 🚀

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 📧 Contact
For questions or support, reach out:
- **Email**: your_email@example.com
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/task-management/issues)

