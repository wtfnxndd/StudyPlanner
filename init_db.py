import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Subjects Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    subject_name TEXT NOT NULL
)
""")
# Study Plans Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS study_plans(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    study_date TEXT NOT NULL,
    study_time TEXT NOT NULL,
    duration TEXT NOT NULL,
    notes TEXT,
    status TEXT DEFAULT 'Pending'
)
""")
# Tasks Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    task_name TEXT NOT NULL,
    due_date TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")