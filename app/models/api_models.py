from pydantic import BaseModel

class DocumentIndexResponse(BaseModel):
    document_name: str
    document_type: str
    chunks: int
    status: str

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]