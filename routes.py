from flask import render_template, request, redirect, url_for, session
from models import (
    create_user,
    get_user,
    get_user_by_email,
    add_subject,
    get_subjects,
    delete_subject,
    get_subject,
    update_subject,
    add_study_plan,
    get_study_plans,
    get_study_plan,
    update_study_plan,
    delete_study_plan,
    complete_study_plan,
    add_task,
    get_tasks,
    get_task,
update_task,
delete_task,
complete_task,
get_dashboard_stats)


def register_routes(app):
   

    # ---------- HOME ----------

    @app.route("/")
    def home():
        return render_template("index.html")

    # ---------- REGISTER ----------

    @app.route("/register", methods=["GET", "POST"])
    def register():

        if request.method == "POST":

            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            password = request.form.get("password", "").strip()

            if not name or not email or not password:
                return "All fields are required!"

            if get_user_by_email(email):
                return "Email already exists!"

            if create_user(name, email, password):
                return redirect(url_for("login"))

            return "Registration Failed!"

        return render_template("register.html")

    # ---------- LOGIN ----------

    @app.route("/login", methods=["GET", "POST"])
    def login():

        if request.method == "POST":

            email = request.form.get("email", "").strip()
            password = request.form.get("password", "").strip()

            user = get_user(email, password)

            if user:
                session["user_id"] = user["id"]
                session["user_name"] = user["name"]

                return redirect(url_for("dashboard"))

            return "Invalid Email or Password"

        return render_template("login.html")

    # ---------- DASHBOARD ----------

    @app.route("/dashboard")
    def dashboard():
        if "user_id" not in session:
            return redirect(url_for("login"))

        stats = get_dashboard_stats(session["user_id"])

        return render_template(
            "dashboard.html",
            name=session["user_name"],
            stats=stats
        )

    # ---------- SUBJECTS ----------

    @app.route("/subjects", methods=["GET", "POST"])
    def subjects():

        if "user_id" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            subject = request.form.get("subject")

            add_subject(session["user_id"], subject)

        subject_list = get_subjects(session["user_id"])

        return render_template(
            "subjects.html",
            subjects=subject_list
        )
    @app.route("/edit_subject/<int:id>", methods=["GET", "POST"])
    def edit_subject(id):

        if "user_id" not in session:
           return redirect(url_for("login"))
        
        if request.method == "POST":

            subject_name = request.form.get("subject")

            update_subject(
                id,
                session["user_id"],
                subject_name
            )

            return redirect(url_for("subjects"))

        subject = get_subject(id, session["user_id"])

        return render_template(
            "edit_subject.html",
            subject=subject
        )  
    @app.route("/delete_subject/<int:id>")
    def delete_subject_route(id):

         if "user_id" not in session:
             return redirect(url_for("login"))

         delete_subject(id, session["user_id"])

         return redirect(url_for("subjects"))  
    

    @app.route("/study_plans", methods=["GET", "POST"])
    def study_plans():

        if "user_id" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            add_study_plan(
                session["user_id"],
                request.form["subject_id"],
                request.form["study_date"],
                request.form["study_time"],
                request.form["duration"],
                request.form["notes"]
            )

            return redirect(url_for("study_plans"))

        subjects = get_subjects(session["user_id"])
        plans = get_study_plans(session["user_id"])

        return render_template(
            "study_plans.html",
            subjects=subjects,
            study_plans=plans
        )
    

    @app.route("/edit_study_plan/<int:id>", methods=["GET", "POST"])
    def edit_study_plan(id):

        if "user_id" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            update_study_plan(
                id,
                session["user_id"],
                request.form["subject_id"],
                request.form["study_date"],
                request.form["study_time"],
                request.form["duration"],
                request.form["notes"]
            )

            return redirect(url_for("study_plans"))

        plan = get_study_plan(id, session["user_id"])
        subjects = get_subjects(session["user_id"])

        return render_template(
            "edit_study_plan.html",
            plan=plan,
            subjects=subjects
        )
    # ---------- LOGOUT ----------
    @app.route("/delete_study_plan/<int:id>")
    def delete_study_plan_route(id):

        if "user_id" not in session:
            return redirect(url_for("login"))

        delete_study_plan(id, session["user_id"])

        return redirect(url_for("study_plans"))


    @app.route("/complete_study_plan/<int:id>")
    def complete_study_plan_route(id):

        if "user_id" not in session:
            return redirect(url_for("login"))

        complete_study_plan(id, session["user_id"])

        return redirect(url_for("study_plans"))

    @app.route("/tasks", methods=["GET", "POST"])
    def tasks():
        if "user_id" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":
            add_task(
                session["user_id"],
                request.form["task_name"],
                request.form["due_date"],
                request.form["priority"]
            )

            return redirect(url_for("tasks"))

        task_list = get_tasks(session["user_id"])

        return render_template(
            "tasks.html",
            tasks=task_list
        )
    
    @app.route("/edit_task/<int:id>", methods=["GET", "POST"])
    def edit_task(id):
        if "user_id" not in session:
            return redirect(url_for("login"))

        if request.method == "POST":

            update_task(
                id,
                session["user_id"],
                request.form["task_name"],
                request.form["due_date"],
                request.form["priority"]
            )

            return redirect(url_for("tasks"))

        task = get_task(id, session["user_id"])

        return render_template(
            "edit_task.html",
            task=task
        )
    
    @app.route("/delete_task/<int:id>")
    def delete_task_route(id):
        if "user_id" not in session:
            return redirect(url_for("login"))

        delete_task(id, session["user_id"])

        return redirect(url_for("tasks"))
    
    @app.route("/complete_task/<int:id>")
    def complete_task_route(id):
        if "user_id" not in session:
            return redirect(url_for("login"))

        complete_task(id, session["user_id"])

        return redirect(url_for("tasks"))

    @app.route("/logout")
    def logout():

        session.clear()

        return redirect(url_for("login"))