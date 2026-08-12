from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    model: str
    usage: Usage


class Usage(BaseModel):
    promptTokenCount: int
    candidatesTokenCount: int
    totalTokenCount: int


class ErrorResponse(BaseModel):
    error: str
    message: str