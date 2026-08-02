from fastapi import FastAPI
from schemas import ChatRequest, ChatResponse
from conversation import Conversation
from ai_service.service import ask_ai

app = FastAPI()

conversations = Conversation()

@app.post("/chat", response_model=ChatResponse)
def chat(data: ChatRequest):
    conversations.add_message("user", data.message)
    response = ask_ai(conversations.get_messages())
    conversations.add_message("model", response["text"])
    return {
        "response": response["text"],
        "model": response["model"],
        "usage": response["usage"]
        }