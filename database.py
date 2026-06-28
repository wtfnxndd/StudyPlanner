import sqlite3

DATABASE = "database.db"


def get_db_connection():
    conn = sqlite3.connect(
        DATABASE,
        timeout=30,
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row

    return conn