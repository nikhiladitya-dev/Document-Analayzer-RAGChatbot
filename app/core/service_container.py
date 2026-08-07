from app.core.logger import logger

from app.services.loader_service import LoaderService
from app.services.document_processor import DocumentProcessor
from app.services.embedding_service import EmbeddingService
from app.services.vectorstore_service import VectorStoreService
from app.services.retrieval_service import RetrievalService
from app.services.indexing_service import IndexingService
from app.services.llm_service import LLMService
from app.services.history_service import HistoryService
from app.services.question_rewriter import QuestionRewriter
from app.services.chat_service import ChatService

from app.chains.rag_chain import RAGChain


class ServiceContainer:

    def __init__(self):

        # Core Services
        self.loader_service = None
        self.document_processor = None
        self.history_service = None

        # Lazy Loaded Services
        self.embedding_service = None
        self.vectorstore_service = None
        self.retrieval_service = None
        self.indexing_service = None
        self.llm_service = None
        self.question_rewriter = None
        self.rag_chain = None
        self.chat_service = None

    def initialize(self):

        logger.info("Initializing core services...")

        self.loader_service = LoaderService()
        self.document_processor = DocumentProcessor()
        self.history_service = HistoryService()

        logger.info("Core services initialized successfully.")

    # Embedding

    def get_embedding_service(self):

        if self.embedding_service is None:

            logger.info("Creating EmbeddingService...")

            self.embedding_service = EmbeddingService()

        return self.embedding_service

    # Vector Store

    def get_vectorstore_service(self):

        if self.vectorstore_service is None:

            logger.info("Creating VectorStoreService...")

            self.vectorstore_service = VectorStoreService(
                self.get_embedding_service()
            )

        return self.vectorstore_service

    # Retrieval

    def get_retrieval_service(self):

        if self.retrieval_service is None:

            logger.info("Creating RetrievalService...")

            self.retrieval_service = RetrievalService(
                self.get_vectorstore_service()
            )

        return self.retrieval_service

    # Indexing

    def get_indexing_service(self):

        if self.indexing_service is None:

            logger.info("Creating IndexingService...")

            self.indexing_service = IndexingService(
                loader_service=self.loader_service,
                document_processor=self.document_processor,
                vector_store_service=self.get_vectorstore_service(),
            )

        return self.indexing_service

    # LLM

    def get_llm_service(self):

        if self.llm_service is None:

            logger.info("Creating LLMService...")

            self.llm_service = LLMService()

        return self.llm_service

    # Question Rewriter

    def get_question_rewriter(self):

        if self.question_rewriter is None:

            logger.info("Creating QuestionRewriter...")

            self.question_rewriter = QuestionRewriter(
                self.get_llm_service()
            )

        return self.question_rewriter

    # RAG Chain

    def get_rag_chain(self):

        if self.rag_chain is None:

            logger.info("Creating RAGChain...")

            self.rag_chain = RAGChain(
                retrieval_service=self.get_retrieval_service(),
                llm_service=self.get_llm_service(),
            )

        return self.rag_chain

    # Chat
    def get_chat_service(self):

        if self.chat_service is None:

            logger.info("Creating ChatService...")

            self.chat_service = ChatService(
                rag_chain=self.get_rag_chain(),
                history_service=self.history_service,
                question_rewriter=self.get_question_rewriter(),
            )

        return self.chat_service


container = ServiceContainer()