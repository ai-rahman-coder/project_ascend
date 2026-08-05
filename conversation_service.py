import logging

from conversation import Conversation
from ai_service.service import ask_ai, ask_ai_stream

logger = logging.getLogger(__name__)

conversations = Conversation()

def chat(message: str):
    conversations.add_message("user", message)
    logger.info("Processing chat request")
    response = ask_ai(conversations.get_messages())
    conversations.add_message("model", response["text"])
    return {
            "response": response["text"],
            "model": response["model"],
            "usage": response["usage"]
            }


def chat_stream(message: str):
    conversations.add_message("user", message)
    logger.info("Processing streaming chat request")
    full_response = ""
    for chunk in ask_ai_stream(conversations.get_messages()):
        full_response += chunk
        yield chunk

    conversations.add_message("model", full_response)