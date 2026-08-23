import logging

from conversation import Conversation
from ai_service.service import ask_ai, ask_ai_stream
from rag.pipeline import build_rag_messages

logger = logging.getLogger(__name__)

def chat(user_id: str, message: str):
    conversations = Conversation(user_id)
    conversations.add_message("user", message)
    logger.info("Processing chat request")
    messages = conversations.get_messages()
    rag_messages = build_rag_messages(messages, message)
    response = ask_ai(rag_messages)
    conversations.add_message("model", response["text"])
    
    return {
            "response": response["text"],
            "model": response["model"],
            "usage": response["usage"]
            }


def chat_stream(user_id: str, message: str):
    conversations = Conversation(user_id)
    conversations.add_message("user", message)
    logger.info("Processing streaming chat request")
    full_response = ""
    for chunk in ask_ai_stream(conversations.get_messages()):
        full_response += chunk
        yield chunk

    conversations.add_message("model", full_response)