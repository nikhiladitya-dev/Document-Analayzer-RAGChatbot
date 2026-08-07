from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import logger
from app.core.service_container import container


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Initializing services...")

    container.initialize()

    logger.info("Application Ready!")

    yield

    logger.info("Shutting down...")


app = FastAPI(
    title="Document RAG Chatbot",
    description="""
Production-grade Retrieval-Augmented Generation (RAG) API
for chatting with uploaded documents.

Features:
- PDF, DOCX and TXT document support
- Intelligent document chunking
- Semantic Retrieval
- Conversational Memory
- Page-based Citations
- Retrieval-Augmented Question Answering
""",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router)