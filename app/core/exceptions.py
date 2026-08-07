class DocumentError(Exception):
    """Base exception for document processing."""


class UnsupportedDocumentTypeError(DocumentError):
    """Raised when the uploaded file type is unsupported."""


class DocumentLoadError(DocumentError):
    """Raised when a document cannot be loaded."""


class DocumentProcessingError(DocumentError):
    """Raised when document processing fails."""