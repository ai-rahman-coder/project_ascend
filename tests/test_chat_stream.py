from fastapi.testclient import TestClient

import database
import conversation_service
from main import app


client = TestClient(app)


def fake_ask_ai_stream(messages):
    yield "This "
    yield "is "
    yield "a "
    yield "streamed "
    yield "response."


def test_chat_stream_with_user_1(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    original_ask_ai_stream = conversation_service.ask_ai_stream
    conversation_service.ask_ai_stream = fake_ask_ai_stream

    try:
        response = client.post(
            "/chat/stream",
            headers={
                "Authorization": "Bearer user_1"
            },
            json={
                "message": "Hello"
            }
        )

        assert response.status_code == 200
        assert response.text == "This is a streamed response."

    finally:
        conversation_service.ask_ai_stream = original_ask_ai_stream



def test_chat_stream_with_invalid_token(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    response = client.post(
        "/chat/stream",
        headers={
            "Authorization": "Bearer invalid_user"
        },
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 401



def test_chat_stream_without_authentication(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    response = client.post(
        "/chat/stream",
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 401



def test_chat_stream_user_isolation(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    original_ask_ai_stream = conversation_service.ask_ai_stream

    def fake_stream(messages):
        user_messages = [
            message["parts"][0]["text"]
            for message in messages
            if message["role"] == "user"
        ]

        yield user_messages[-1]

    conversation_service.ask_ai_stream = fake_stream

    try:
        user_1_response = client.post(
            "/chat/stream",
            headers={
                "Authorization": "Bearer user_1"
            },
            json={
                "message": "Docker"
            }
        )

        user_2_response = client.post(
            "/chat/stream",
            headers={
                "Authorization": "Bearer user_2"
            },
            json={
                "message": "Kubernetes"
            }
        )

        assert user_1_response.status_code == 200
        assert user_2_response.status_code == 200

        assert user_1_response.text == "Docker"
        assert user_2_response.text == "Kubernetes"

    finally:
        conversation_service.ask_ai_stream = original_ask_ai_stream