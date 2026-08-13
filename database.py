import sqlite3


def get_connection():
    return sqlite3.connect("ascend.db")


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_message(user_id, role, content):
    connection = get_connection()

    connection.execute(
        """INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)""",
        (user_id, role, content)
    )

    connection.commit()
    connection.close()


def get_messages(user_id):
    connection = get_connection()

    cursor = connection.execute("""
        SELECT role, content
        FROM messages
        WHERE user_id = ?
        ORDER BY id""",
        (user_id,)
    )

    rows = cursor.fetchall()

    connection.close()

    return rows