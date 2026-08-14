import logging_config.logger

import database
database.initialize_database()

from fastapi import Depends, FastAPI
from auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from schemas import ChatRequest, ChatResponse
from conversation_service import chat as chat_service, chat_stream as chat_stream_service

from exceptions.ai_exceptions import ProviderUnavailableError, UnauthorizedAccessError
from exceptions.handlers import provider_unavailable_handler, unauthorized_access_handler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ProviderUnavailableError, provider_unavailable_handler)
app.add_exception_handler(UnauthorizedAccessError, unauthorized_access_handler)

@app.post("/chat", response_model=ChatResponse)
def chat(
        data: ChatRequest,
        user_id: str = Depends(get_current_user)
    ):
    return chat_service(user_id, data.message)

@app.post("/chat/stream", response_class=StreamingResponse)
def chat_stream(
        data: ChatRequest,
        user_id: str = Depends(get_current_user)
    ):
    return StreamingResponse(chat_stream_service(user_id, data.message), media_type="text/plain")