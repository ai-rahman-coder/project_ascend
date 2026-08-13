import sqlite3


def get_connection():
    return sqlite3.connect("ascend.db")


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_message(role, content):
    connection = get_connection()

    connection.execute(
        "INSERT INTO messages (role, content) VALUES (?, ?)",
        (role, content)
    )

    connection.commit()
    connection.close()


def get_messages():
    connection = get_connection()

    cursor = connection.execute("""
        SELECT role, content
        FROM messages
        ORDER BY id
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows