from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.logger import logger


class DocumentProcessor:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            add_start_index=True,
        )

    def process(
        self,
        documents: list[Document],
    ) -> list[Document]:

        logger.info("Starting document chunking...")

        chunks = self.text_splitter.split_documents(documents)

        for chunk_id, chunk in enumerate(chunks):

            chunk.metadata.update(
                {
                    "chunk_id": chunk_id,
                    "end_index": (
                        chunk.metadata["start_index"]
                        + len(chunk.page_content)
                    ),
                }
            )

        logger.info(
            f"Generated {len(chunks)} chunks."
        )

        return chunks