from langchain_core.documents import Document

from app.core.logger import logger
from app.prompts.rag_prompt import RAG_PROMPT
from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService


class RAGChain:

    def __init__(
        self,
        retrieval_service: RetrievalService,
        llm_service: LLMService,
    ):
        self.retrieval_service = retrieval_service
        self.llm_service = llm_service

    def invoke(
        self,
        question: str,
    ) -> dict:

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        logger.info("Running RAG chain...")

        documents = self.retrieval_service.retrieve(
            query=question,
        )

        context = self._format_context(documents)

        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        answer = self.llm_service.invoke(prompt)

        logger.info("RAG response generated successfully.")
        logger.info(f"Retrieved Metadata: {documents[0].metadata}")

        return {
            "answer": answer,
            "sources": [
                {
                    "source": document.metadata.get("source"),
                    "page": document.metadata.get("page"),
                    "chunk_id": document.metadata.get("chunk_id"),
                    "content": document.page_content,
                }
                for document in documents
            ],
        }

    def _format_context(
        self,
        documents: list[Document],
    ) -> str:

        logger.info("Formatting retrieved context...")

        sections = []

        for document in documents:

            source = document.metadata.get(
                "source",
                "Unknown",
            )

            page = document.metadata.get(
                "page",
                "N/A",
            )

            section = (
                f"Source: {source}\n"
                f"Page: {page}\n\n"
                f"{document.page_content}"
            )

            sections.append(section)

        return "\n\n" + ("-" * 60 + "\n\n").join(sections)