from pathlib import Path

from app.core.logger import logger

from app.services.loader_service import LoaderService
from app.services.document_processor import DocumentProcessor
from app.services.vectorstore_service import VectorStoreService


class IndexingService:


    def __init__(
        self,
        loader_service: LoaderService,
        document_processor: DocumentProcessor,
        vector_store_service: VectorStoreService,
    ):
        self.loader_service = loader_service
        self.document_processor = document_processor
        self.vector_store_service = vector_store_service


    def index_document(
        self,
        file_path: str,
    ):

        logger.info("Starting document indexing...")


        # Clear the old documents from the vector databse
        self.vector_store_service.delete_collection()

        # Load the document
        documents = self.loader_service.load(file_path)

        # Chunk the document
        chunks = self.document_processor.process(documents)

        # Store chunks in the vector database
        self.vector_store_service.add_documents(chunks)

        logger.info("Document indexed successfully.")

        return {
            "document_name": Path(file_path).name,
            "document_type": Path(file_path).suffix.lower(),
            "chunks": len(chunks),
            "status": "success",
        }

    def reindex_document(
        self,
        file_path: str,
    ):

        logger.info("Re-indexing document...")

        self.vector_store_service.delete_collection()

        return self.index_document(file_path)