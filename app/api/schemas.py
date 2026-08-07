from pydantic import BaseModel
from typing import List


class DocumentIndexResponse(BaseModel):

    status: str
    document_name: str
    document_type: str
    chunks: int


class ChatRequest(BaseModel):

    question: str


class SourceChunk(BaseModel):

    source: str
    page: int | None = None
    chunk_id: int
    content: str


class ChatResponse(BaseModel):

    answer: str
    sources: List[SourceChunk]