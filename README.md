📚 Study Planner

A web-based Study Planner developed using python, Flask, SQLite, HTML, CSS, and Bootstrap. The application helps students organize subjects, create study plans, manage daily tasks, and monitor their study progress through an interactive dashboard.

---

Features
 User Authentication

* User Registration
* User Login
* Secure Session Management
* Logout
 Subject Management

* Add Subjects
* View Subjects
* Edit Subjects
* Delete Subjects

Study Planner

* Create Study Plans
* View Study Plans
* Edit Study Plans
* Delete Study Plans
* Mark Study Plans as Completed

 Daily Tasks

* Add Daily Tasks
* View Tasks
* Edit Tasks
* Delete Tasks
* Mark Tasks as Completed
 Dashboard

* Total Subjects
* Total Study Plans
* Completed Study Plans
* Total Tasks
* Progress Statistics

---
 Technologies Used

* Python 3
* Flask
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* Jinja2

---
 Project Structure

```
StudyPlanner/
│
├── app.py
├── database.py
├── init_db.py
├── models.py
├── routes.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── subjects.html
│   ├── edit_subject.html
│   ├── study_plans.html
│   ├── edit_study_plan.html
│   ├── tasks.html
│   └── edit_task.html
│
├── static/
│
└── README.md
```

---
Installation
 1. Clone the repository

```bash
git clone https://github.com/wtfnxndd/StudyPlanner.git
```
 2. Open the project

```bash
cd StudyPlanner
```
 3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

 5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create the database

```bash
python init_db.py
```

 7. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

Database

The application uses **SQLite** and includes the following tables:

* users
* subjects
* study_plans
* tasks

---

Future Enhancements

* Email reminders
* Calendar integration
* Study analytics charts
* Password reset
* Notifications
* Export reports as PDF
* Dark mode

---
 Learning Outcomes

This project demonstrates:

* Flask Web Development
* CRUD Operations
* SQLite Database Management
* Session Management
* MVC-style Project Structure
* HTML & Bootstrap UI
* Software Testing Project Development

Author

Nandan R

MCA Student

License

This project is developed for academic and learning purposes.
