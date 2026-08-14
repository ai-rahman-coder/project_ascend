from fastapi.testclient import TestClient

import database
import conversation_service
from main import app


client = TestClient(app)


def fake_ask_ai(messages):
    return {
        "text": "This is a test AI response.",
        "model": "test-model",
        "usage": {
            "promptTokenCount": 10,
            "candidatesTokenCount": 5,
            "totalTokenCount": 15
        }
    }


def test_chat_with_user_1(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    original_ask_ai = conversation_service.ask_ai
    conversation_service.ask_ai = fake_ask_ai

    try:
        response = client.post(
            "/chat",
            headers={
                "Authorization": "Bearer user_1"
            },
            json={
                "message": "What is Docker?"
            }
        )

        assert response.status_code == 200

        data = response.json()

        assert data["response"] == "This is a test AI response."
        assert data["model"] == "test-model"
        assert data["usage"]["totalTokenCount"] == 15

    finally:
        conversation_service.ask_ai = original_ask_ai


def test_chat_with_invalid_token(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    response = client.post(
        "/chat",
        headers={
            "Authorization": "Bearer invalid_user"
        },
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 401



def test_chat_without_authentication(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    response = client.post(
        "/chat",
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 401



def test_chat_user_isolation(tmp_path):
    database.DATABASE_PATH = str(tmp_path / "test.db")
    database.initialize_database()

    original_ask_ai = conversation_service.ask_ai

    def fake_ask_ai(messages):
        user_messages = [
            message["parts"][0]["text"]
            for message in messages
            if message["role"] == "user"
        ]

        return {
            "text": user_messages[-1],
            "model": "test-model",
            "usage": {
                "promptTokenCount": 1,
                "candidatesTokenCount": 1,
                "totalTokenCount": 2
            }
        }

    conversation_service.ask_ai = fake_ask_ai

    try:
        user_1_response = client.post(
            "/chat",
            headers={
                "Authorization": "Bearer user_1"
            },
            json={
                "message": "Docker"
            }
        )

        user_2_response = client.post(
            "/chat",
            headers={
                "Authorization": "Bearer user_2"
            },
            json={
                "message": "Kubernetes"
            }
        )

        assert user_1_response.status_code == 200
        assert user_2_response.status_code == 200

        assert user_1_response.json()["response"] == "Docker"
        assert user_2_response.json()["response"] == "Kubernetes"

    finally:
        conversation_service.ask_ai = original_ask_ai