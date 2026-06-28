from database import get_db_connection


def create_user(name, email, password):
    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, password)
        )

        conn.commit()
        return True

    except Exception as e:
        print("Error:", e)
        return False

    finally:
        conn.close()


def get_user(email, password):
    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM users
            WHERE email = ? AND password = ?
            """,
            (email, password)
        )

        user = cursor.fetchone()
        return user

    finally:
        conn.close()


def get_user_by_email(email):
    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM users
            WHERE email = ?
            """,
            (email,)
        )

        return cursor.fetchone()

    finally:
        conn.close()
        # ---------- SUBJECTS ----------

def add_subject(user_id, subject_name):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO subjects(user_id, subject_name) VALUES(?,?)",
            (user_id, subject_name)
        )

        conn.commit()

    finally:
        conn.close()


def get_subjects(user_id):

    conn = get_db_connection()

    try:

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM subjects WHERE user_id=?",
            (user_id,)
        )

        return cursor.fetchall()

    finally:
        conn.close()

def delete_subject(subject_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM subjects WHERE id=? AND user_id=?",
            (subject_id, user_id)
        )

        conn.commit()

    finally:
        conn.close()


def get_subject(subject_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM subjects WHERE id=? AND user_id=?",
            (subject_id, user_id)
        )

        return cursor.fetchone()

    finally:
        conn.close()

def update_subject(subject_id, user_id, subject_name):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE subjects
            SET subject_name=?
            WHERE id=? AND user_id=?
            """,
            (subject_name, subject_id, user_id)
        )

        conn.commit()

    finally:
        conn.close()
# ---------- STUDY PLANS ----------

def add_study_plan(user_id, subject_id, study_date, study_time, duration, notes):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO study_plans
            (user_id, subject_id, study_date, study_time, duration, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            subject_id,
            study_date,
            study_time,
            duration,
            notes
        ))

        conn.commit()

    finally:
        conn.close()


def get_study_plans(user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT study_plans.*,
                   subjects.subject_name
            FROM study_plans
            JOIN subjects
            ON study_plans.subject_id = subjects.id
            WHERE study_plans.user_id = ?
            ORDER BY study_date, study_time
        """, (user_id,))

        return cursor.fetchall()

    finally:
        conn.close()
def get_study_plan(plan_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM study_plans
            WHERE id=? AND user_id=?
        """, (plan_id, user_id))

        return cursor.fetchone()

    finally:
        conn.close()


def update_study_plan(plan_id, user_id,
                      subject_id,
                      study_date,
                      study_time,
                      duration,
                      notes):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE study_plans

            SET
            subject_id=?,
            study_date=?,
            study_time=?,
            duration=?,
            notes=?

            WHERE id=? AND user_id=?

        """, (
            subject_id,
            study_date,
            study_time,
            duration,
            notes,
            plan_id,
            user_id
        ))

        conn.commit()

    finally:
        conn.close()


def delete_study_plan(plan_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM study_plans
            WHERE id=? AND user_id=?
        """, (plan_id, user_id))

        conn.commit()

    finally:
        conn.close()
def complete_study_plan(plan_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE study_plans
            SET status='Completed'
            WHERE id=? AND user_id=?
        """, (plan_id, user_id))

        conn.commit()

    finally:
        conn.close()        
# ---------------- TASKS ----------------

def add_task(user_id, task_name, due_date, priority):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tasks
            (user_id, task_name, due_date, priority)
            VALUES (?, ?, ?, ?)
        """, (
            user_id,
            task_name,
            due_date,
            priority
        ))

        conn.commit()

    finally:
        conn.close()


def get_tasks(user_id):

    conn = get_db_connection()

    try:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE user_id=?
            ORDER BY due_date
        """, (user_id,))

        return cursor.fetchall()

    finally:
        conn.close()        
def get_task(task_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tasks
            WHERE id=? AND user_id=?
        """, (task_id, user_id))

        return cursor.fetchone()

    finally:
        conn.close()


def update_task(task_id, user_id,
                task_name,
                due_date,
                priority):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks

            SET
            task_name=?,
            due_date=?,
            priority=?

            WHERE id=? AND user_id=?

        """, (
            task_name,
            due_date,
            priority,
            task_id,
            user_id
        ))

        conn.commit()

    finally:
        conn.close()


def delete_task(task_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM tasks
            WHERE id=? AND user_id=?
        """, (task_id, user_id))

        conn.commit()

    finally:
        conn.close()


def complete_task(task_id, user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tasks
            SET status='Completed'
            WHERE id=? AND user_id=?
        """, (task_id, user_id))

        conn.commit()

    finally:
        conn.close()

def get_dashboard_stats(user_id):

    conn = get_db_connection()

    try:
        cursor = conn.cursor()

        stats = {}

        cursor.execute(
            "SELECT COUNT(*) AS total FROM subjects WHERE user_id=?",
            (user_id,)
        )
        stats["subjects"] = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COUNT(*) AS total FROM study_plans WHERE user_id=?",
            (user_id,)
        )
        stats["study_plans"] = cursor.fetchone()["total"]

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM study_plans
            WHERE user_id=? AND status='Completed'
            """,
            (user_id,)
        )
        stats["completed_plans"] = cursor.fetchone()["total"]

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM tasks
            WHERE user_id=?
            """,
            (user_id,)
        )
        stats["tasks"] = cursor.fetchone()["total"]

        cursor.execute(
            """
            SELECT COUNT(*) AS total
            FROM tasks
            WHERE user_id=? AND status='Completed'
            """,
            (user_id,)
        )
        stats["completed_tasks"] = cursor.fetchone()["total"]

        conn.close()

        return stats

    except:
        conn.close()
        return None