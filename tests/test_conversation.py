import database

from conversation import Conversation


def test_conversation_add_and_get_messages(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")

    database.initialize_database()

    conversation = Conversation("user_1")

    conversation.add_message(
        "user",
        "What is Docker?"
    )

    messages = conversation.get_messages()

    assert messages == [
        {
            "role": "user",
            "parts": [
                {
                    "text": "What is Docker?"
                }
            ]
        }
    ]



def test_conversation_is_separated_by_user(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")

    database.initialize_database()

    user_1 = Conversation("user_1")
    user_2 = Conversation("user_2")

    user_1.add_message(
        "user",
        "What is Docker?"
    )

    user_2.add_message(
        "user",
        "What is Kubernetes?"
    )

    user_1_messages = user_1.get_messages()
    user_2_messages = user_2.get_messages()

    assert user_1_messages[0]["parts"][0]["text"] == "What is Docker?"
    assert user_2_messages[0]["parts"][0]["text"] == "What is Kubernetes?"

    assert "Kubernetes" not in str(user_1_messages)
    assert "Docker" not in str(user_2_messages)