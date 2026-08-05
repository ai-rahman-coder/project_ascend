import logging_config.logger

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from schemas import ChatRequest, ChatResponse
from conversation_service import chat as chat_service, chat_stream as chat_stream_service

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(data: ChatRequest):
    return chat_service(data.message)

@app.post("/chat/stream", response_class=StreamingResponse)
def chat_stream(data: ChatRequest):
    return StreamingResponse(chat_stream_service(data.message), media_type="text/plain")