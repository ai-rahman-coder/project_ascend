from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    model: str
    usage: dict


class Usage(BaseModel):
    promptTokenCount: int
    candidatesTokenCount: int
    totalTokenCount: int