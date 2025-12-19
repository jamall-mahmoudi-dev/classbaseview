
# Django Task Manager

This is a simple “Task / Todo application” built with “Django” using  
“Class-Based Views (CBV)” and “Django Authentication”.

Each user can:
- Log in
- Create tasks
- View only their own tasks
- Update tasks
- Delete tasks

The project is designed for *learning Django fundamentals deeply, especially:
- Request → Response flow
- Authentication
- Class-Based Views
- Secure querysets
- Templates

---

Features

- User authentication (login / logout)
- Task ownership (each task belongs to a user)
- CRUD operations for tasks
- Secure access using `LoginRequiredMixin`
- Clean project structure
- SQLite database (default Django setup)

---

Project Structure

config/
│
├── settings.py
├── urls.py
│
tasks/
│
├── models.py
├── views.py
├── urls.py
├── forms.py
│
templates/
│
├── base.html
├── login.html
│
tasks/templates/tasks/
│
├── task_list.html
├── task_form.html
├── task_confirm_delete.html
└── task_detail.html

---

Requirements

- Python 3.10+
- Django 5.2+

---

Installation & Setup

Clone the project

```bash
git clone <your-repository-url>
cd django-task-manager

Create and activate a virtual environment
python -m venv venv
Activate it:
•	Windows:
venv\Scripts\activate
•	Linux / macOS:
source venv/bin/activate

Install dependencies
pip install django

Run database migrations
python manage.py migrate

Create a superuser (admin)
python manage.py createsuperuser
Follow the prompts to create a username and password.

Run the development server
python manage.py runserver
Open your browser and go to:
http://127.0.0.1:8000/

Authentication Flow
1.	Open the site (/)
2.	You will be redirected to /login/
3.	Log in using your credentials
4.	After login, you will be redirected to the task list
5.	You can now create, edit, and delete your tasks
6.	Logout using /logout/

How the Request Flow Works (High-Level)
Browser
 → URL configuration
 → Class-Based View
 → Authentication check
 → Database query
 → Template rendering
 → HTTP Response

Task Model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
Each task:
•	Belongs to exactly one user
•	Cannot be accessed by other users

Security Design
All task-related views use:
LoginRequiredMixin
and filtered querysets:
Task.objects.filter(user=self.request.user)
This ensures:
•	Users only see their own tasks
•	URL manipulation does not expose other users’ data

Learning Goals of This Project
This project helps you understand:
•	How Django handles requests internally
•	How Class-Based Views work
•	How authentication and sessions work
•	How templates receive data from views
•	How to build secure multi-user applications

Possible Improvements
•	Pagination for task list
•	Task status toggle (done / undone)
•	Success messages
•	REST API with Django REST Framework
•	Unit tests

Author
Built for learning and practicing Django
Feel free to modify, extend, and experiment 

 License
This project is open for educational use.

---devops523@gmail.com

