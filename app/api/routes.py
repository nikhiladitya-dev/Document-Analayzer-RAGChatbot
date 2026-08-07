from pathlib import Path
import shutil
import traceback

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
)

from app.api.schemas import (
    DocumentIndexResponse,
    ChatRequest,
    ChatResponse,
    SourceChunk,
)

from app.core.config import DOCUMENTS_DIR
from app.core.exceptions import (
    UnsupportedDocumentTypeError,
    DocumentLoadError,
)

from app.core.service_container import container


router = APIRouter(
    prefix="/api/v1",
    tags=["Document RAG"],
)


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}


@router.post(
    "/upload-document",
    response_model=DocumentIndexResponse,
)
def upload_document(
    file: UploadFile = File(...),
):

    try:

        suffix = Path(file.filename).suffix.lower()

        if suffix not in SUPPORTED_EXTENSIONS:

            raise UnsupportedDocumentTypeError(
                f"Unsupported document type: {suffix}"
            )

        DOCUMENTS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = DOCUMENTS_DIR / file.filename

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        response = (
            container
            .get_indexing_service()
            .index_document(
                str(file_path)
            )
        )

        return DocumentIndexResponse(
            status=response["status"],
            document_name=response["document_name"],
            document_type=response["document_type"],
            chunks=response["chunks"],
        )

    except UnsupportedDocumentTypeError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except DocumentLoadError as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
):

    try:

        response = (
            container
            .get_chat_service()
            .ask(
                question=request.question,
            )
        )

        sources = [

            SourceChunk(
                source=source["source"],
                page=source["page"],
                chunk_id=source["chunk_id"],
                content=source["content"],
            )

            for source in response["sources"]

        ]

        return ChatResponse(

            answer=response["answer"],

            sources=sources,

        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get("/health")
def health():

    return {

        "status": "healthy",

        "service": "Document Analyzer Chatbot",

        "version": "1.0.0",

    }