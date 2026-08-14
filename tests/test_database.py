import sqlite3

import database


def test_add_and_get_message(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")

    database.initialize_database()

    database.add_message(
        "user_1",
        "user",
        "What is Docker?"
    )

    messages = database.get_messages("user_1")

    assert messages == [
        ("user", "What is Docker?")
    ]


def test_messages_are_separated_by_user(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")

    database.initialize_database()

    database.add_message(
        "user_1",
        "user",
        "What is Docker?"
    )

    database.add_message(
        "user_2",
        "user",
        "What is Kubernetes?"
    )

    user_1_messages = database.get_messages("user_1")
    user_2_messages = database.get_messages("user_2")

    assert user_1_messages == [
        ("user", "What is Docker?")
    ]

    assert user_2_messages == [
        ("user", "What is Kubernetes?")
    ]